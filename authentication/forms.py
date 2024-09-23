from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']




class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
