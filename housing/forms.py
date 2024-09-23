from django import forms
from .models import Housing

class HousingForm(forms.ModelForm):
    class Meta:
        model = Housing
        fields = [
            'title', 'address', 'city', 'state', 'zipcode', 
            'description', 'price', 'bedrooms', 'bathrooms', 
            'garage', 'sqft', 'lot_size', 'available_units',
            'photo_main', 'photo_1', 'is_published'
        ]
