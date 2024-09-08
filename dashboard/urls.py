from django.urls import path
from dashboard.views import *


urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('properties/', property.as_view(), name='properties'),
    path('reviews/', Review.as_view(), name='reviews'),
    path('bookings/', Booking.as_view(), name='bookings'),
    path('profile/', Profile.as_view(), name='profile'),


]