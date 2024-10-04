from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path
from django.contrib.auth import views as auth_views


class UserRegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'auth-page.html'
    success_url = reverse_lazy('auth')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserUpdateForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('profile')







from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  
            return redirect('property')  
        else:
            messages.error(request, 'Invalid username or password')  

    return render(request, 'auth-page.html')

