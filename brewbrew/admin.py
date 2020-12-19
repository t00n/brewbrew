from django.contrib import admin
from .models import (
    Ingredient,
    RecipeMashingIngredient,
    RecipeBrewingStep,
    RecipeBoilingIngredient,
    RecipeWhirlpoolIngredient,
    RecipeYeast,
    RecipeFermentationStep,
    RecipeAdjunct,
    Recipe,
)


class IngredientAdmin(admin.ModelAdmin):
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


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
