from django.shortcuts import render, redirect
from django.views import View

from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView


# Create your views here.
class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard.html')
    

class PropertyView(View):
    def get(self, request):
        properties = Housing.objects.all()
        return render(request, 'properties.html', {'properties': properties})

    def post(self, request):
        # Handling the form submission from the modal
        location = request.POST.get('location')
        price = request.POST.get('price')
        bedrooms = request.POST.get('bedrooms')
        square_footage = request.POST.get('square-footage')
        amenities = request.POST.get('amenities')
        media = request.FILES.getlist('media')

        # Create and save the new property
        property = Housing.objects.create(
            address=location,
            price=price,
            bedrooms=bedrooms,
            sqft=square_footage,
            description=amenities,
            photo_main=media[0] if media else None,  # Handle main image, or use a placeholder
        )
        
        # Optionally handle additional media like videos or images
        for file in media[1:]:
            HousingImage.objects.create(housing=property, image=file)
        
        return redirect('property-list')  # Redirect to the property list after successful submission

    
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
    
