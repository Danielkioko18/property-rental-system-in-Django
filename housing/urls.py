from django.urls import path
from housing.views import *


urlpatterns = [
    # path('', Index.as_view(), name='index'),
    path('auth/', Auth.as_view(), name='auth'), 

    # path('about/', About.as_view(), name='about'),
    # path('contact/', Contact.as_view(), name='contact'),
    path('property/', Property.as_view(), name='property'),
    path('property-details/', PropertyDetails.as_view(), name='property-details'),
    path('', PropertyListing.as_view(), name='listings'),


]