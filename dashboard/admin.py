from django.contrib import admin
from .models import Housing, HousingImage

class HousingImageInline(admin.TabularInline):
    model = HousingImage
    extra = 1  

class HousingAdmin(admin.ModelAdmin):
    inlines = [HousingImageInline]

admin.site.register(Housing, HousingAdmin)
