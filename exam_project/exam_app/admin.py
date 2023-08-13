from django.contrib import admin
from .models import PlaceType, Place, PlaceDetail, City

@admin.register(PlaceType)
class PlaceTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'city']
    list_filter = ['category', 'city']
    search_fields = ['name', 'city']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
