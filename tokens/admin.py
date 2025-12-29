from django.contrib import admin

from .models import SaddleBagToken

# Register your models here.

@admin.register(SaddleBagToken)
class SaddleBagTokenAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')