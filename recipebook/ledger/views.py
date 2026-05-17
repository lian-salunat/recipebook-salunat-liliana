from django.shortcuts import render, get_object_or_404

from .models import Recipe


def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes_list.html', {'recipes': recipes})


def recipe(request, pk):
    recipe_obj = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe.html', {'recipe': recipe_obj})
