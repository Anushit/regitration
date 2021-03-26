from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email','first_name','last_name','mobile','is_staff','is_active']
    search_fields = ['email']
    list_per_page = 5
admin.site.register(User,UserAdmin)