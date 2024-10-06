from django.contrib.auth.models import AbstractUser
from django.db import models

from .manager import CustomUserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)  
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['first_name', 'last_name']  

    obj = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.user.email