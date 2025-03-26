from django.urls import path
from .views import pokemon_view

urlpatterns = [
    path('', pokemon_view, name='pokemon_search'),
]