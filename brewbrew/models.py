from django.db import models


class Ingredient(models.Model):
    variety = models.CharField(max_length=50, help_text="Name/variety of the ingredient")
    unit = models.CharField(max_length=10, help_text="Unit of measure of the ingredient")

    def __str__(self):
        return self.variety


class Supplier(models.Model):
    name = models.CharField(max_length=50, help_text="Name of the supplier")


class IngredientBatch(models.Model):
    ingredient = models.ForeignKey(Ingredient,
        on_delete=models.RESTRICT, help_text="Ingredient")
    producer = models.ForeignKey(Supplier, 
        on_delete=models.RESTRICT, help_text="Supplier")
    batch_number = models.CharField(max_length=50, help_text="Batch number")
    bill_number = models.CharField(max_length=50, help_text="Bill number")
    quantity = models.FloatField(help_text="Quantity in the batch")


class Tank(models.Model):
    name = models.CharField(max_length=50, help_text="Name/number of the tank")


class RecipeMashingIngredient(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    mashing_ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)
    quantity = models.FloatField(help_text="Quantity to use in the recipe")


class BrewingStep(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    temperature = models.FloatField(help_text="Temperature during this brewing step")
    duration = models.IntegerField(help_text="Duration of this brewing step in minutes")


class RecipeBoilingIngredient(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    boiling_ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)
    quantity = models.FloatField(help_text="Quantity to use in the recipe")
    time = models.IntegerField(help_text="When to add the ingredient (in minutes from the end of boiling)")


class RecipeWhirlpoolIngredient(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    whirlpool_ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)
    quantity = models.FloatField(help_text="Quantity to use in the recipe")


class RecipeYeasts(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    yeast = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)
    quantity = models.FloatField(help_text="Quantity to use in the recipe")


class FermentationStep(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    temperature = models.FloatField(help_text="Temperature during this fermentation step")
    duration = models.IntegerField(help_text="Duration of this fermentation step in days")


class RecipeAdjuncts(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    yeast = models.ForeignKey(Ingredient, on_delete=models.RESTRICT)
    quantity = models.FloatField(help_text="Quantity to use in the recipe")


class Recipe(models.Model):
    name = models.CharField(max_length=50, help_text="Name of the recipe")
    recipe = models.TextField(help_text="Written description of the recipe")

    # Mashing
    mashing_ingredients = models.ManyToManyField(
        Ingredient, through=RecipeMashingIngredient,
        related_name="recipe_mashing", help_text="Ingredients to add during mashing")
    mashing_water_quantity = models.FloatField(help_text="Liters of water to add during mashing")

    # Brewing
    # cf BrewingStep

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
        Ingredient, through=RecipeYeasts, 
        related_name="recipe_yeasts", help_text="Yeasts to add before fermentation")
    # cf FermentationStep

    # Adjuncts/Dryhopping
    adjuncts = models.ManyToManyField(
        Ingredient, through=RecipeAdjuncts, 
        related_name="recipe_adjuncts", help_text="Adjuncts/Hops to add during fermentation")

    def __str__(self):
        return self.name


class Brew(models.Model):
    original_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    recipe = models.TextField()
    fermentation_time = models.IntegerField()
    fermentation_tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    dry_hopping_time = models.IntegerField()
    dry_hopping_hop1 = models.ForeignKey(Ingredient, null=True, blank=True, on_delete=models.CASCADE, related_name='brew_dry_hopping_hop1')
    dry_hopping_hop1_quantity = models.FloatField(null=True, blank=True)
    dry_hopping_hop2 = models.ForeignKey(Ingredient, null=True, blank=True, on_delete=models.CASCADE, related_name='brew_dry_hopping_hop2')
    dry_hopping_hop2_quantity = models.FloatField(null=True, blank=True)
    dry_hopping_hop3 = models.ForeignKey(Ingredient, null=True, blank=True, on_delete=models.CASCADE, related_name='brew_dry_hopping_hop3')
    dry_hopping_hop3_quantity = models.FloatField(null=True, blank=True)
