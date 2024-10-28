from django.urls import path
from dashboard.views import *


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('properties/', PropertyView.as_view(), name='properties'),
    path('reviews/', Review.as_view(), name='reviews'),
    path('bookings/', Booking.as_view(), name='bookings'),
    path('profile/', Profile.as_view(), name='profile'),
    path('housing/create/', HousingCreateView.as_view(), name='housing_create'),
    path('housing/<int:pk>/update/', HousingUpdateView.as_view(), name='housing_update'),

    path('property/delete/<int:pk>/', PropertyDeleteView.as_view(), name='property-delete'),
    path('revenue-data/', RevenueDataView.as_view(), name='revenue-data'),
    path('property/tenants/', PropertyTenantsView.as_view(), name='property-tenants'),
]

