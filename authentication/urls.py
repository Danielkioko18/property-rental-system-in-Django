from django.urls import path
from .views import UserRegisterView, UserUpdateView

urlpatterns = [
    path('profile/update/', UserUpdateView.as_view(), name='profile_update'),
    path('', UserRegisterView.as_view(), name='auth'), 
 
]
