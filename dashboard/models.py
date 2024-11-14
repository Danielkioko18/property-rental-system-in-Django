from django.db import models
from authentication.models import User
from django.utils.text import slugify
from django.utils import timezone
from datetime import date
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

class Tenant(models.Model):
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, related_name='tenants')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    house_no = models.CharField(max_length=20)
    
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    water_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    date_added = models.DateField(default=timezone.now)
    
    @property
    def period(self):
        """Calculate the period in months from date_added to the current date."""
        today = date.today()
        months = (today.year - self.date_added.year) * 12 + (today.month - self.date_added.month)
        return months if months > 0 else 1  # Ensures at least 1 month
    
    @property
    def total_rent(self):
        """Calculate total rent as monthly rent multiplied by the number of months stayed."""
        return self.monthly_rent * self.period

    @property
    def total_bill(self):
        """Calculate total bill as total rent plus water bill."""
        return self.total_rent + self.water_bill

    @property
    def balance(self):
        """Calculate balance as total bill minus paid amount."""
        return self.total_bill - self.paid

    def save(self, *args, **kwargs):
        if not self.monthly_rent:
            self.monthly_rent = self.housing.price 
        
        #self.total_rent = self.monthly_rent * self.period
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.housing}"


class Payment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property = models.ForeignKey(Housing, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_date = models.DateTimeField(auto_now_add=True)
    invoice_number = models.PositiveIntegerField(unique=True)

    def save(self, *args, **kwargs):
        # Automatically generate the invoice number without checking form input
        last_payment = Payment.objects.all().order_by('-id').first()
        if last_payment:
            self.invoice_number = last_payment.invoice_number + 1
        else:
            self.invoice_number = 1  # Start from 1

        super().save(*args, **kwargs)
