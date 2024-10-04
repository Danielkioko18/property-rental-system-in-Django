from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', UserRegisterView.as_view(), name='auth'),
 

   path('login/', custom_login_view, name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/update/', UserUpdateView.as_view(), name='profile_update'),
]
