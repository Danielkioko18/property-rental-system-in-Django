from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
 
    # path('login/', auth_views.LoginView.as_view(template_name='auth-page.html'), name='login'),
    path('login/', custom_login_view, name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('profile/update/', UserUpdateView.as_view(), name='profile'),
]