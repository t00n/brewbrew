from datetime import date
from django.shortcuts import render, redirect
from django.http import Http404

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
        'original_recipes': Recipe.objects.all()
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

def create_brew(request, id):
	if request.method == "GET":
		try:
			recipe = Recipe.objects.get(pk=id)
			tank = Tank.objects.get(pk=int(request.GET["tank_id"]))
		except:
			pass
		else:
			brew = recipe.create_brew(tank)

			return redirect(f'/admin/brewbrew/brew/{brew.id}/change')

	raise Http404("Page does not exist")