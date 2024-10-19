from django.db import models
from authentication.models import User
from django.utils.text import slugify
import uuid

class Housing(models.Model):
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, related_name='houses')
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField()
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    available_units = models.IntegerField(default=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            # Create a slug using title and a portion of the UUID
            unique_id = str(uuid.uuid4())[:8]  # You can use more or fewer characters from the UUID
            self.slug = slugify(self.title) + '-' + unique_id
        super().save(*args, **kwargs)

class HousingImage(models.Model):
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return f"Image for {self.housing.title}"
