from django.shortcuts import render, redirect
from django.views import View

from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404

from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Sum
from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Sum
from .models import Housing

from django.shortcuts import render
from django.db.models import Sum
from .models import Housing
from django.http import JsonResponse
from django.views import View


from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, Q
from django.views import View
from .models import Housing,Tenant,Payment



from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, Q
from django.views import View
from .models import Housing
from django.db.models.functions import TruncMonth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from decimal import Decimal

class DashboardView(View):
    def get(self, request):
        
        query = request.GET.get('q')
        if query:
            properties = Housing.objects.filter(
                Q(title__icontains=query) | Q(address__icontains=query) | Q(city__icontains=query)
            )
        else:
            properties = Housing.objects.all()

        # Dynamic stats for the dashboard
        total_properties = Housing.objects.count()
        total_units = Housing.objects.aggregate(total_units=Sum('available_units'))['total_units'] or 0
        total_revenue = Housing.objects.aggregate(total_revenue=Sum('price'))['total_revenue'] or 0

        context = {
            'properties': properties,
            'total_properties': total_properties,
            'total_units': total_units,
            'total_revenue': total_revenue,
        }
        return render(request, 'dashboard.html', context)


class RevenueDataView(View):
    def get(self, request):
        # Retrieve revenue from properties sold or rented
        monthly_revenue = Housing.objects.annotate(month=TruncMonth('date_sold')).values('month').annotate(
            monthly_revenue=Sum('price')).order_by('month')

        # Initialize placeholder for 12 months
        revenue_data = [0] * 12
        for entry in monthly_revenue:
            month_index = entry['month'].month - 1  # Adjust month for 0-indexed array
            revenue_data[month_index] = entry['monthly_revenue'] or 0

        return JsonResponse({'monthly_revenue': revenue_data})


class PropertyView(View):
    def get(self, request):
        properties = Housing.objects.all()
        return render(request, 'properties.html', {'properties': properties})

    def post(self, request):
        title = request.POST.get('title')
        location = request.POST.get('location')
        city = request.POST.get('city')
        state = request.POST.get('state')
        price = request.POST.get('price')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        garage = request.POST.get('garage')
        sqft = request.POST.get('sqft')
        lot_size = request.POST.get('lot_size')
        description = request.POST.get('description')
        media = request.FILES.getlist('images')
        
        if not description:
            return render(request, 'properties.html', {
                'error': 'Description is required!',
                'properties': Housing.objects.all()
            })

        landlord = request.user 
        property = Housing.objects.create(
            landlord=landlord,  
            title=title,
            address=location,
            city=city,
            state=state,
            price=price,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            garage=garage,
            sqft=sqft,
            lot_size=lot_size,
            description=description,
            photo_main=media[0] if media else None,  
        )
        
        for file in media[1:]:
            HousingImage.objects.create(housing=property, image=file)
        
        return redirect('properties')


class PropertyDeleteView(View):
    def post(self, request, pk):
        property = get_object_or_404(Housing, pk=pk)
        property.delete()
        return redirect('properties')


class Review(View):
    def get(self, request):
        return render(request, 'reviews.html')
    
class Booking(View):
    def get(self, request):
        return render(request, 'bookings.html')
    
class Profile(View):
    def get(self, request):
        return render(request, 'profile.html')
    

class HousingCreateView(LoginRequiredMixin, CreateView):
    model = Housing
    form_class = HousingForm
    template_name = 'housing_form.html'
    success_url = reverse_lazy('housing_list')

    def form_valid(self, form):
        form.instance.landlord = self.request.user  
        return super().form_valid(form)


class HousingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Housing
    form_class = HousingForm
    template_name = 'housing_form.html'
    success_url = reverse_lazy('housing_list')

    def test_func(self):
        housing = self.get_object()
        return self.request.user == housing.landlord


class PropertyTenantsView(View):
    def get(self, request, pk):
        # Get the property using the primary key (pk)
        property = get_object_or_404(Housing, pk=pk)

        # Get all tenants related to this property (assuming you have a related Tenant model)
        tenants = Tenant.objects.filter(housing=property)
        # Get the total number of tenants for this property
        total_tenants = tenants.count()

        
        return render(request, 'tenants.html', {'tenants':tenants, 'property': property, 'total_tenants': total_tenants})  
    
    def post(self, request, pk):
        # Get tenant ID from the POST data
        tenant_id = request.POST.get('tenant_id')
        
        # Get the tenant to delete, if it exists
        tenant = get_object_or_404(Tenant, id=tenant_id, housing_id=pk)
        
        # Delete the tenant
        tenant.delete()
        
        # Redirect back to the same page after deletion
        return HttpResponseRedirect(reverse('property-tenants', args=[pk]))


class AddTenantView(View):
    def post(self, request, pk):
        # Retrieve the housing property instance based on the primary key
        housing = get_object_or_404(Housing, pk=pk)

        # Capture data from the form in the modal
        tenant_name = request.POST.get('tenant_name')
        phone_number = request.POST.get('phone_number')
        house_number = request.POST.get('house_number')
        
        # Create a new Tenant instance and save it
        tenant = Tenant.objects.create(
            name=tenant_name,
            phone=phone_number,
            house_no=house_number,
            housing=housing  
        )
        
        # Redirect to the tenants view for this specific property
        return redirect('property-tenants', pk=pk)


class AddPaymentView(View):
    def post(self, request):
        tenant_id = request.POST.get("tenant_id")
        amount = float(request.POST.get("amount"))

        tenant = get_object_or_404(Tenant, id=tenant_id)
        tenant.paid += Decimal(amount)  # Update the paid field with the new amount
        tenant.save()

        # Create a new Payment entry
        payment = Payment(
            tenant=tenant,
            property=tenant.housing,
            amount=Decimal(amount)
        )
        payment.save()

        messages.success(request, "Payment added successfully!")
        return redirect("property-tenants", pk=tenant.housing_id)

class PaymentListView(View):
    def get(self, request, property_id):
        # Fetch payments for the given property
        property = get_object_or_404(Housing, id=property_id)
        payments = Payment.objects.filter(property=property).order_by('-paid_date')

        # Pass payments to the template
        return render(request, 'payments.html', {
            'payments': payments,
            'property': property,
        })