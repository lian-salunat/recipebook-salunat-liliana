from django.urls import path

from .views import recipes_list, recipe

app_name = 'ledger'

urlpatterns = [
    path('recipes/', recipes_list, name='recipes_list'),
    path('recipe/<int:pk>/', recipe, name='recipe'),
]