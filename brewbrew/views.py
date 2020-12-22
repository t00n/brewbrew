from datetime import date, datetime, timezone
from collections import defaultdict
from django.shortcuts import render, redirect
from django.http import Http404

from .models import Brew, Recipe, Tank, IngredientBatchInput, BrewAdjunctBatch

def home(request):
    return render(request, 'home.html')

def stock(request):
	now = datetime.now()
	stock_entries = []

	# add all the inputs of ingredients until now
	for batch_input in IngredientBatchInput.objects.filter(input_time__lte=now):
		stock_entries.append({
			'date': batch_input.input_time,
			'brew': '',  # no brew because it's an input
			'name': batch_input.ingredient_batch.ingredient.variety,
			'supplier': batch_input.ingredient_batch.ingredient.supplier.name,
			'bill': batch_input.bill_number,
			'batch': batch_input.ingredient_batch.batch_number,
			'quantity': batch_input.quantity,
			'unit': batch_input.ingredient_batch.ingredient.unit,
		})

	# add the outputs from all brews until now
	for brew in Brew.objects.filter(start_date__lte=now.date()):
		# brewing/mashing
		for bmib in brew.brewmashingingredientbatch_set.all():
			stock_entries.append({
				'date': brew.brew_start_time,
				'brew': brew.batch_name,
				'name': bmib.ingredient_batch.ingredient.variety,
				'supplier': bmib.ingredient_batch.ingredient.supplier.name,
				'bill': '',  # no bill number because we cannot know where this came from
				'batch': bmib.ingredient_batch.batch_number,
				'quantity': -bmib.quantity,
				'unit': bmib.ingredient_batch.ingredient.unit,
			})

		# boiling
		for bbib in brew.brewboilingingredientbatch_set.all():
			stock_entries.append({
				'date': brew.boiling_start_time,
				'brew': brew.batch_name,
				'name': bbib.ingredient_batch.ingredient.variety,
				'supplier': bbib.ingredient_batch.ingredient.supplier.name,
				'bill': '',  # no bill number because we cannot know where this came from
				'batch': bbib.ingredient_batch.batch_number,
				'quantity': -bbib.quantity,
				'unit': bbib.ingredient_batch.ingredient.unit,
			})

		# whirlpool
		for bwib in brew.brewwhirlpoolingredientbatch_set.all():
			stock_entries.append({
				'date': brew.whirlpool_start_time,
				'brew': brew.batch_name,
				'name': bwib.ingredient_batch.ingredient.variety,
				'supplier': bwib.ingredient_batch.ingredient.supplier.name,
				'bill': '',  # no bill number because we cannot know where this came from
				'batch': bwib.ingredient_batch.batch_number,
				'quantity': -bwib.quantity,
				'unit': bwib.ingredient_batch.ingredient.unit,
			})

		# yeasts
		for byb in brew.brewyeastbatch_set.all():
			stock_entries.append({
				'date': brew.cooling_end_time,  # cooling end time is the same as fermentation start time
				'brew': brew.batch_name,
				'name': byb.yeast_batch.ingredient.variety,
				'supplier': byb.yeast_batch.ingredient.supplier.name,
				'bill': '',  # no bill number because we cannot know where this came from
				'batch': byb.yeast_batch.batch_number,
				'quantity': -byb.quantity,
				'unit': byb.yeast_batch.ingredient.unit,
			})

	# add the outputs from fermentations until now
	for bab in BrewAdjunctBatch.objects.filter(date__lte=now.date()):
		stock_entries.append({
			'date': datetime.combine(bab.date, datetime.max.time(), tzinfo=timezone.utc),
			'brew': bab.brew.batch_name,
			'name': bab.ingredient_batch.ingredient.variety,
			'supplier': bab.ingredient_batch.ingredient.supplier.name,
			'bill': '',  # no bill number because we cannot know where this came from
			'batch': bab.ingredient_batch.batch_number,
			'quantity': -bab.quantity,
			'unit': bab.ingredient_batch.ingredient.unit,
		})

	# sort all entries by date
	stock_entries = sorted(stock_entries, key=lambda x: x['date'])

	# count the cumulative total quantity by ingredient/supplier
	current_stock = defaultdict(lambda: 0)
	for entry in stock_entries:
		current_stock[entry['name']+entry['supplier']] += entry['quantity']
		entry['total_quantity'] = current_stock[entry['name']+entry['supplier']]

	# sort by reversed date for display
	stock_entries = reversed(stock_entries)

	return render(request, 'stock.html', {
		'stock_entries': stock_entries,
	})

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