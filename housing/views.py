from django.shortcuts import render
from django.views import View

from django.views.generic import ListView
from dashboard.models import Housing
from django.shortcuts import get_object_or_404
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
    def get(self, request, slug):
        property = get_object_or_404(Housing, slug=slug)
        return render(request, 'view.html', {'property': property})

    
class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')

class PropertyListing(ListView):    
    model = Housing
    template_name = 'listings.html'
    context_object_name = 'houses'
    paginate_by = 10

    def get_queryset(self):
        queryset = Housing.objects.filter(is_published=True)
        # You can add custom filtering logic here based on the search form
        location = self.request.GET.get('location')
        price_range = self.request.GET.get('price-range')
        bedrooms = self.request.GET.get('bedrooms')
        if location:
            queryset = queryset.filter(city__icontains=location)
        if price_range:
            min_price, max_price = map(int, price_range.split('-')) if '-' in price_range else (60000, None)
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price if max_price else float('inf'))
        if bedrooms:
            queryset = queryset.filter(bedrooms__gte=bedrooms)
        return queryset


