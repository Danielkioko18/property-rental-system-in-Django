from django.shortcuts import render
from django.views import View

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
    


    
