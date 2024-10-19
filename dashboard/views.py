from django.shortcuts import render, redirect
from django.views import View

from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView

class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard.html')
    

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
    
