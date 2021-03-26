from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'Firstname','lastname','email']
    search_fields = ['username']
    list_per_page = 5

admin.site.register(Employee,EmployeeAdmin)