from django.shortcuts import render

from .forms import RecipeForm

def recipes(request):
    return render(request, 'recipes.html', {"create_form": RecipeForm})
