from django.contrib import admin

from .models import Ingredient, Profile, Recipe, RecipeImage, RecipeIngredient


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, RecipeImageInline]
    list_display = ('name', 'author', 'created_on', 'updated_on')
