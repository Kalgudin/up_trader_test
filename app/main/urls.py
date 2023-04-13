from django.urls import path

from .views import main_page, other_pages

urlpatterns = [
    path('', main_page),
    path('menu/<str:menu_item>', other_pages),
]
