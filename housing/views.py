from django.shortcuts import render
from django.views import View

from django.views.generic import ListView
from dashboard.models import Housing
# Create your views here.

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

class PropertyListing(ListView):    
    model = Housing
    template_name = 'listings.html'
    context_object_name = 'houses'
    paginate_by = 10

    def get_queryset(self):
        return Housing.objects.filter(is_published=True)

