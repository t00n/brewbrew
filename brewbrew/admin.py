from django.contrib import admin
from .models import (
    Ingredient,
    IngredientBatch,
    Supplier,
    Tank,
    RecipeMashingIngredient,
    RecipeBrewingStep,
    RecipeBoilingIngredient,
    RecipeWhirlpoolIngredient,
    RecipeYeast,
    RecipeFermentationStep,
    RecipeAdjunct,
    Recipe,
)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(IngredientBatch)
class IngredientBatchAdmin(admin.ModelAdmin):
    pass


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(Tank)
class TankAdmin(admin.ModelAdmin):
    pass


class RecipeMashingIngredientInline(admin.TabularInline):
    model = RecipeMashingIngredient
    extra = 1


class RecipeBrewingStepInline(admin.TabularInline):
    model = RecipeBrewingStep
    extra = 1


class RecipeBoilingIngredientInline(admin.TabularInline):
    model = RecipeBoilingIngredient
    extra = 1


class RecipeWhirlpoolIngredientInline(admin.TabularInline):
    model = RecipeWhirlpoolIngredient
    extra = 0


class RecipeYeastInline(admin.TabularInline):
    model = RecipeYeast
    extra = 1


class RecipeFermentationStepInline(admin.TabularInline):
    model = RecipeFermentationStep
    extra = 1


class RecipeAdjunctInline(admin.TabularInline):
    model = RecipeAdjunct
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        RecipeMashingIngredientInline,
        RecipeBrewingStepInline,
        RecipeBoilingIngredientInline,
        RecipeWhirlpoolIngredientInline,
        RecipeYeastInline,
        RecipeFermentationStepInline,
        RecipeAdjunctInline,
    ]
