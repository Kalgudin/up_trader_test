from django.contrib import admin
from .models import *


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'tag', 'level', 'parent', 'url']
    ordering = ('level', 'name', 'tag')
