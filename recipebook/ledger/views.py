from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Recipe, RecipeImage


def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes_list.html', {'recipes': recipes})


@login_required
def recipe(request, pk):
    recipe_obj = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe.html', {'recipe': recipe_obj})


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name']
    template_name = 'recipe_add.html'

    def get_success_url(self):
        return reverse_lazy('ledger:recipe', kwargs={'pk': self.object.pk})


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    fields = ['image', 'description']
    template_name = 'recipe_add_image.html'

    def form_valid(self, form):
        form.instance.recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'ledger:recipe',
            kwargs={'pk': self.kwargs['pk']},
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        return context

