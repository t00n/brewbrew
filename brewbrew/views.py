from datetime import date
from django.shortcuts import render

from .forms import RecipeForm
from .models import Brew, Recipe, Tank

def home(request):
    return render(request, 'home.html')

def tanks(request):
    today = date.today()
    tanks = {t: None for t in Tank.objects.all()}
    for brew in Brew.objects.all():
        if today <= brew.end_date:
        	if brew.fermentation_tank is not None:
	            assert tanks[brew.fermentation_tank] is None
	            tanks[brew.fermentation_tank] = brew
    
    return render(request, 'tanks.html', {
        'tanks': list(tanks.items()),
    })

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
