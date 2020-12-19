from django.shortcuts import render

from .forms import RecipeForm
from .models import Recipe

def recipes(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)

        if form.is_valid():
            Recipe.objects.create(**form.cleaned_data)

    recipes = Recipe.objects.all().order_by('name')

    return render(request, 'recipes.html', {
        "create_form": RecipeForm,
        "recipes": recipes
    })
