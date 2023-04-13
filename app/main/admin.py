from django.contrib import admin
from .models import *


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'parent', 'url']
    ordering = ('level', 'name',)
