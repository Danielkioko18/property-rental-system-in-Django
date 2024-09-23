from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class UserRegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'auth-page.html'
    success_url = reverse_lazy('login')  



class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('profile')  

    def get_object(self, queryset=None):
        return self.request.user  
