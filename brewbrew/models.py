from enum import Enum

from django.db import models


class IngredientType(Enum):
    GRAIN = "Grain"
    HOP = "Hop"
    YEAST = "Yeast"
    ADJUNCT = "Adjunct"
    FRUIT = "Fruit"


class Ingredient(models.Model):
    type = models.CharField(max_length=50, choices=[(tag.name, tag.value) for tag in IngredientType],
        help_text="The type of ingredient")
    variety = models.CharField(max_length=50, help_text="Name/variety of the ingredient")
    unit = models.CharField(max_length=10, help_text="Unit of measure of the ingredient")

    class Meta:
        unique_together = ['type', 'variety']

    def __str__(self):
        return f'{self.variety} ({self.unit})'


class Supplier(models.Model):
    name = models.CharField(max_length=50, help_text="Name of the supplier")


class IngredientBatch(models.Model):
    ingredient = models.ForeignKey(Ingredient,
        on_delete=models.PROTECT, help_text="Ingredient")
    supplier = models.ForeignKey(Supplier, 
        on_delete=models.PROTECT, help_text="Supplier")
    batch_number = models.CharField(max_length=50, help_text="Batch number")
    bill_number = models.CharField(max_length=50, help_text="Bill number")
    quantity = models.FloatField(help_text="Quantity in the batch")


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


class BrewMashingIngredientBatch(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    ingredient_batch = models.ForeignKey(IngredientBatch, on_delete=models.PROTECT)
    quantity = models.FloatField(help_text="Quantity to use in the brew")


class BrewBrewingStep(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    temperature = models.FloatField(help_text="Temperature during this brewing step")
    duration = models.IntegerField(help_text="Duration of this brewing step in minutes")


class BrewBoilingIngredientBatch(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    ingredient_batch = models.ForeignKey(IngredientBatch, on_delete=models.PROTECT)
    quantity = models.FloatField(help_text="Quantity to use in the brew")
    time = models.IntegerField(help_text="When the ingredient was added (in minutes from the end of boiling)")


class BrewWhirlpoolIngredientBatch(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    ingredient_batch = models.ForeignKey(IngredientBatch, on_delete=models.PROTECT)
    quantity = models.FloatField(help_text="Quantity to use in the brew")


class BrewYeastBatch(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    yeast_batch = models.ForeignKey(IngredientBatch, on_delete=models.PROTECT)
    quantity = models.FloatField(help_text="Quantity to use in the brew")


class BrewFermentationStep(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, help_text="Name of the fermentation step")
    temperature = models.FloatField(help_text="Temperature during this fermentation step")
    duration = models.IntegerField(help_text="Duration of this fermentation step in days")


class BrewFermentationAnalysis(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    day = models.IntegerField(help_text="Day number from the start of fermentation when the analysis occured")
    plateau_degree_or_density = models.FloatField(help_text="Gravity expressed in °p or sg")


class BrewAdjunctBatch(models.Model):
    brew = models.ForeignKey("Brew", on_delete=models.CASCADE)
    ingredient_batch = models.ForeignKey(IngredientBatch, on_delete=models.PROTECT)
    quantity = models.FloatField(help_text="Quantity to use in the brew")


class Brew(models.Model):
    # meta info
    original_recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    batch_name = models.CharField(max_length=50, help_text="Batch name")

    # general info
    start_date = models.DateField(help_text="Date to start brewing")
    total_quantity = models.IntegerField(help_text="Quantity of beer obtained with this brew", null=True, blank=True)

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
    fermentation_tank = models.ForeignKey(Tank, on_delete=models.PROTECT, help_text="Tank in which to ferment")
    fermentation_comments = models.TextField(null=True, blank=True)
    # cf BrewFermentationStep
    # cf BrewFermentationAnalysis

    # Adjuncts/Dryhopping
    adjuncts_start_time = models.DateTimeField("Start of the adjuncts/dryhopping stage", null=True, blank=True)
    adjuncts = models.ManyToManyField(
        IngredientBatch, through=BrewAdjunctBatch, 
        related_name="brew_adjuncts", help_text="Adjuncts/Hops to add during fermentation")

    def __str__(self):
        return self.name
