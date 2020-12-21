from enum import Enum
from datetime import timedelta, datetime

from django.db import models


class IngredientType(Enum):
    GRAIN = "Grain"
    HOP = "Hop"
    YEAST = "Yeast"
    ADJUNCT = "Adjunct"
    FRUIT = "Fruit"


class Supplier(models.Model):
    name = models.CharField(max_length=50, help_text="Name of the supplier")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    type = models.CharField(max_length=50, choices=[(tag.name, tag.value) for tag in IngredientType],
        help_text="The type of ingredient")
    variety = models.CharField(max_length=50, help_text="Name/variety of the ingredient")
    supplier = models.ForeignKey(Supplier, 
        on_delete=models.PROTECT, help_text="Supplier")
    unit = models.CharField(max_length=10, help_text="Unit of measure of the ingredient")

    class Meta:
        unique_together = ['type', 'variety']

    def __str__(self):
        return f'{self.variety} {self.supplier} ({self.unit})'


class IngredientBatch(models.Model):
    ingredient = models.ForeignKey(Ingredient,
        on_delete=models.PROTECT, help_text="Ingredient")
    batch_number = models.CharField(max_length=50, help_text="Batch number")
    bill_number = models.CharField(max_length=50, help_text="Bill number")
    quantity = models.FloatField(help_text="Quantity in the batch")

    def __str__(self):
        return f"{self.ingredient.variety} {self.ingredient.supplier} ({self.batch_number})"


class Tank(models.Model):
    name = models.CharField(max_length=50, help_text="Name/number of the tank", unique=True)
    capacity = models.IntegerField(help_text="Capacity in liters")

    def __str__(self):
        return f'Tank {self.name}'


class RecipeMashingIngredient(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.FloatField(help_text="Quantity to use in the recipe")


class RecipeBrewingStep(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    temperature = models.FloatField(help_text="Temperature during this brewing step")
    duration = models.IntegerField(help_text="Duration of this brewing step in minutes")


class RecipeBoilingIngredient(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.FloatField(help_text="Quantity to use in the recipe")
    time = models.IntegerField(help_text="When to add the ingredient (in minutes from the end of boiling)")


class RecipeWhirlpoolIngredient(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.FloatField(help_text="Quantity to use in the recipe")


class RecipeYeast(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    yeast = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.FloatField(help_text="Quantity to use in the recipe")


class RecipeFermentationStep(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, help_text="Name of the fermentation step")
    temperature = models.FloatField(help_text="Temperature during this fermentation step")
    duration = models.IntegerField(help_text="Duration of this fermentation step in days")


class RecipeAdjunct(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.FloatField(help_text="Quantity to use in the recipe")
    day = models.IntegerField(help_text="Day to add the adjunct/hop (from the start of fermentation)")


class Recipe(models.Model):
    name = models.CharField(max_length=50, help_text="Name of the recipe")

    # Mashing
    mashing_ingredients = models.ManyToManyField(
        Ingredient, through=RecipeMashingIngredient,
        related_name="recipe_mashing", help_text="Ingredients to add during mashing")
    mashing_water_quantity = models.FloatField(help_text="Liters of water to add during mashing")

    # Brewing
    # cf RecipeBrewingStep

    # Filtration
    filtration_water_quantity = models.FloatField(help_text="Liters of waters to add during filtration")

    # Boiling
    boiling_duration = models.IntegerField(help_text="Duration of boiling step in minutes")
    boiling_ingredients = models.ManyToManyField(
        Ingredient, through=RecipeBoilingIngredient,
        related_name="recipe_boiling", help_text="Ingredients to add during boiling")


    # Whirlpool
    whirlpool_ingredients = models.ManyToManyField(
        Ingredient, through=RecipeWhirlpoolIngredient,
        related_name="recipe_whirlpool", help_text="Ingredients to add during whirlpool")

    # Cooling
    # Nothing to see here...

    # Fermentation
    yeasts = models.ManyToManyField(
        Ingredient, through=RecipeYeast, 
        related_name="recipe_yeasts", help_text="Yeasts to add before fermentation")
    # cf RecipeFermentationStep

    # Adjuncts/Dryhopping
    adjuncts = models.ManyToManyField(
        Ingredient, through=RecipeAdjunct, 
        related_name="recipe_adjuncts", help_text="Adjuncts/Hops to add during fermentation")

    def __str__(self):
        return self.name


    def create_brew(self):
        brew = Brew()
        brew.original_recipe = self
        brew.start_date = datetime.now().date()
        brew.mashing_water_quantity = self.mashing_water_quantity
        brew.filtration_water_quantity = self.filtration_water_quantity
        brew.boiling_duration = self.boiling_duration
        brew.save()

        # Mashing
        for mashing_ingredient in self.recipemashingingredient_set.all():
            brew.brewmashingingredientbatch_set.create(
                    brew=brew,
                    ingredient=mashing_ingredient.ingredient,
                    quantity=mashing_ingredient.quantity,
            )

        for boiling_ingredient in self.recipeboilingingredient_set.all():
            brew.brewboilingingredientbatch_set.create(
                    brew=brew,
                    ingredient=boiling_ingredient.ingredient,
                    quantity=boiling_ingredient.quantity,
                    time=boiling_ingredient.time,
            )

        for whirlpool_ingredient in self.recipeboilingingredient_set.all():
            brew.brewboilingingredientbatch_set.create(
                    brew=brew,
                    ingredient=whirlpool_ingredient.ingredient,
                    quantity=whirlpool_ingredient.quantity,
            )

        for yeast in self.recipeyeast_set.all():
            brew.brewyeastbatch_set.create(
                    brew=brew,
                    yeast=yeast.yeast,
                    quantity=yeast.quantity,
            )

        for adjunct in self.recipeadjunct_set.all():
            brew.brewadjunctbatch_set.create(
                    brew=brew,
                    ingredient=adjunct.ingredient,
                    quantity=adjunct.quantity,
                    date=brew.start_date + timedelta(days=adjunct.day)
            )

        return brew


class BrewMashingIngredientBatch(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    ingredient_batch = models.ForeignKey(IngredientBatch, null=True, blank=True, on_delete=models.PROTECT)
    quantity = models.FloatField(help_text="Quantity to use in the brew")


class BrewBrewingStep(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    temperature = models.FloatField(help_text="Temperature during this brewing step")
    duration = models.IntegerField(help_text="Duration of this brewing step in minutes")


class BrewBoilingIngredientBatch(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    ingredient_batch = models.ForeignKey(IngredientBatch, null=True, blank=True, on_delete=models.PROTECT)
    quantity = models.FloatField(help_text="Quantity to use in the brew")
    time = models.IntegerField(
        null=True, blank=True, help_text="When the ingredient was added (in minutes from the end of boiling)")


class BrewWhirlpoolIngredientBatch(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    ingredient_batch = models.ForeignKey(IngredientBatch, null=True, blank=True, on_delete=models.PROTECT)
    quantity = models.FloatField(help_text="Quantity to use in the brew")


class BrewYeastBatch(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    yeast = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    yeast_batch = models.ForeignKey(IngredientBatch, null=True, blank=True, on_delete=models.PROTECT)
    quantity = models.FloatField(help_text="Quantity to use in the brew")


class BrewFermentationStep(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, help_text="Name of the fermentation step")
    temperature = models.FloatField(help_text="Temperature during this fermentation step")
    duration = models.IntegerField(help_text="Duration of this fermentation step in days")

    class Meta:
        verbose_name_plural = "Fermentation steps"


class BrewFermentationAnalysis(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    day = models.IntegerField(help_text="Day number from the start of fermentation when the analysis occured")
    plato_degree_or_density = models.FloatField(help_text="Gravity expressed in °p or sg")

    class Meta:
        verbose_name_plural = "Fermentation analysis"


class BrewAdjunctBatch(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    ingredient_batch = models.ForeignKey(IngredientBatch, null=True, blank=True, on_delete=models.PROTECT)
    quantity = models.FloatField(help_text="Quantity to use in the brew")
    date = models.DateField(help_text="Date when the adjunct/hop was added")

    class Meta:
        verbose_name = "Fermentation agents/Dry hopping"


class Brew(models.Model):
    # meta info
    original_recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    batch_name = models.CharField(max_length=50, help_text="Batch name")

    # general info
    start_date = models.DateField(help_text="Date to start brewing")
    total_quantity = models.PositiveIntegerField(
        help_text="Quantity of beer obtained with this brew in liters", null=True, blank=True)

    # Mashing
    mashing_ingredients = models.ManyToManyField(
        IngredientBatch, through=BrewMashingIngredientBatch,
        related_name="brew_mashing", help_text="Ingredients to add during mashing")
    mashing_water_quantity = models.FloatField(help_text="Liters of water to add during mashing")

    # Brewing
    brew_start_time = models.DateTimeField("Start of the brewing stage", null=True, blank=True)
    brew_comments = models.TextField(null=True, blank=True)
    # cf BrewBrewingStep

    # Filtration
    filtration_start_time = models.DateTimeField("Start of the filtration stage", null=True, blank=True)
    filtration_water_quantity = models.FloatField(help_text="Liters of waters to add during filtration")

    # Boiling
    boiling_start_time = models.DateTimeField("Start of the boiling stage", null=True, blank=True)
    boiling_duration = models.IntegerField(help_text="Duration of boiling step in minutes")
    boiling_ingredients = models.ManyToManyField(
        IngredientBatch, through=BrewBoilingIngredientBatch,
        related_name="brew_boiling", help_text="Ingredients to add during boiling")


    # Whirlpool
    whirlpool_start_time = models.DateTimeField("Start of the whirlpool stage", null=True, blank=True)
    whirlpool_ingredients = models.ManyToManyField(
        IngredientBatch, through=BrewWhirlpoolIngredientBatch,
        related_name="brew_whirlpool", help_text="Ingredients to add during whirlpool")

    # Cooling
    cooling_start_time = models.DateTimeField("Start of the cooling stage", null=True, blank=True)
    cooling_end_time = models.DateTimeField("End of the cooling stage", null=True, blank=True)

    # Fermentation
    yeasts = models.ManyToManyField(
        IngredientBatch, through=BrewYeastBatch, 
        related_name="brew_yeasts", help_text="Yeasts to add before fermentation")
    fermentation_tank = models.ForeignKey(Tank, null=True, blank=True,
        on_delete=models.PROTECT, help_text="Tank in which to ferment")
    fermentation_comments = models.TextField(null=True, blank=True)
    # cf BrewFermentationStep
    # cf BrewFermentationAnalysis

    # Adjuncts/Dryhopping
    adjuncts_start_time = models.DateTimeField("Start of the adjuncts/dryhopping stage", null=True, blank=True)
    adjuncts = models.ManyToManyField(
        IngredientBatch, through=BrewAdjunctBatch, 
        related_name="brew_adjuncts", help_text="Adjuncts/Hops to add during fermentation")

    def __str__(self):
        return self.batch_name

    @property
    def end_date(self):
        days = sum(step.duration for step in self.brewfermentationstep_set.all())
        return self.start_date + timedelta(days=days)

    @property
    def fermentation_steps(self):
        res = []
        start_date = self.start_date
        for step in self.brewfermentationstep_set.all():
            end_date = start_date + timedelta(days=step.duration)
            res.append((start_date, end_date, step))
            start_date = end_date
        return res
