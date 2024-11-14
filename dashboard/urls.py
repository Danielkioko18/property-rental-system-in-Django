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
    path('property/<int:pk>/tenants/', PropertyTenantsView.as_view(), name='property-tenants'),
    path('property/<int:property_id>/payments/', PaymentListView.as_view(), name='payment_list'),
    path('property/<int:pk>/tenants/add-tenant/', AddTenantView.as_view(), name='add_tenant'),
    path('dashboard/property/tenants/add-payment/', AddPaymentView.as_view(), name='add_payment'),

]

