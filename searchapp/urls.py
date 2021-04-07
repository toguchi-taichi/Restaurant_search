from django.urls import path, include
from django.conf import settings
from .views import map_func, search_func

urlpatterns = [
    path('', search_func),
    path('map/', map_func, name='map'),
    path('search/', search_func, name='search'),
] 