from django.shortcuts import render
from django.views import View

# Create your views here.

class Auth(View):
    def get(self, request):
        return render(request, 'auth-page.html')
class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    
class About(View):
    def get(self, request):
        return render(request, 'about.html')
    
class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')
    
class Property(View):
    def get(self, request):
        return render(request, 'property.html')
    
class PropertyDetails(View):
    def get(self, request):
        return render(request, 'view.html')
    
class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')

class PropertyListing(View):
    def get(self, request):
        return render(request, 'listings.html')
