from django.contrib import admin
from .models import User, AdminUser

# Register your models here.

@admin.register(AdminUser)
class AdminUser(admin.ModelAdmin):
    list_display = ['username', 'email']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

# @admin.register(AllUser)
# class AllUserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'password', 'email', 'is_superuser']
#     list_filter = ['is_staff']

# @admin.register(StuffUser)
# class StuffUserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'password', 'email', 'is_superuser']

#     def get_queryset(self, request):
#         """Filter users to show only non-staff members."""
#         return super().get_queryset(request).filter(is_staff=False)