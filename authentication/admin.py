from django.contrib import admin
from .models import User

# # Register your models here.
admin.site.register(User)



# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User
# from .forms import UserCreationForm, UserUpdateForm

# class UserAdmin(UserAdmin):
#     add_form = UserCreationForm
#     form = UserUpdateForm
#     model = User

#     list_display = ['email', 'first_name', 'last_name', 'is_staff']
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal Info', {'fields': ('first_name', 'last_name')}),
#         ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)

# admin.site.register(User, UserAdmin)
