from django.contrib import admin
from .models import Menu


@admin.register(Menu)
class ManuAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'url']
    ordering = ('level', 'name',)
