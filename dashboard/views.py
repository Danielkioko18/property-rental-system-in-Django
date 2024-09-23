from django.shortcuts import render
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
    
class property(View):
    def get(self, request):
        return render(request, 'properties.html')
    
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
    
