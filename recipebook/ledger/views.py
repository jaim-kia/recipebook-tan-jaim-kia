from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe, Ingredient

def recipes(request):
	recipes = Recipe.objects.all()
	ctx = { "recipes:": recipe }
	return render(request, 'recipes.html', ctx)

def recipe(request, pk):
	ingredients = Ingredient.objects.filter(recipe__recipe__name="Recipe {}".format(pk))
	ctx = { "ingredients:": ingredients }
	return render(request, 'recipe.html', ctx)

class RecipeListView(ListView):
	model = Recipe
	template_name = "recipes.html"


class RecipeDetailView(DetailView):
	model = Recipe
	template_name = "recipe.html"