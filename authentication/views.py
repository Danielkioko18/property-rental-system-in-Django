from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


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

