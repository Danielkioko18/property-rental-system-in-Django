from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import *
from .models import *

class UserRegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'auth-page.html'
    success_url = reverse_lazy('login')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserUpdateForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('profile')


def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  
            return redirect('dashboard')  
        else:
            messages.error(request, 'Invalid email or password')  

    return render(request, 'auth-page.html')


def custom_logout_view(request):
    logout(request)  
    messages.success(request, 'You have been successfully logged out.')  
    return redirect('login')  
