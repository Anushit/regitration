from django.contrib import admin
from .models import artist

# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name','description','image','created_at','updated_at']
    search_fields = ['Name']
    list_per_page = 5

admin.site.register(artist,ArtistAdmin)