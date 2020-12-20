from django.contrib import admin
from fieldsets_with_inlines import FieldsetsInlineMixin
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
    BrewMashingIngredientBatch,
    BrewBrewingStep,
    BrewBoilingIngredientBatch,
    BrewWhirlpoolIngredientBatch,
    BrewYeastBatch,
    BrewFermentationStep,
    BrewFermentationAnalysis,
    BrewAdjunctBatch,
    Brew,
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
class RecipeAdmin(FieldsetsInlineMixin, admin.ModelAdmin):
    fieldsets_with_inlines = [
        ('General', {'fields': ['name']}),
        ('Mashing', {'fields': ['mashing_water_quantity']}),
        RecipeMashingIngredientInline,
        RecipeBrewingStepInline,
        ('Filtration', {'fields': ['filtration_water_quantity']}),
        ('Boiling', {'fields': ['boiling_duration']}),
        RecipeBoilingIngredientInline,
        RecipeWhirlpoolIngredientInline,
        RecipeYeastInline,
        RecipeFermentationStepInline,
        RecipeAdjunctInline,
    ]

class BrewMashingIngredientBatchInline(admin.TabularInline):
    model = BrewMashingIngredientBatch
    extra = 1


class BrewBrewingStepInline(admin.TabularInline):
    model = BrewBrewingStep
    extra = 1


class BrewBoilingIngredientBatchInline(admin.TabularInline):
    model = BrewBoilingIngredientBatch
    extra = 1


class BrewWhirlpoolIngredientBatchInline(admin.TabularInline):
    model = BrewWhirlpoolIngredientBatch
    extra = 0


class BrewYeastBatchInline(admin.TabularInline):
    model = BrewYeastBatch
    extra = 1


class BrewFermentationStepInline(admin.TabularInline):
    model = BrewFermentationStep
    extra = 1


class BrewFermentationAnalysisInline(admin.TabularInline):
    model = BrewFermentationAnalysis
    extra = 2


class BrewAdjunctBatchInline(admin.TabularInline):
    model = BrewAdjunctBatch
    extra = 0


@admin.register(Brew)
class BrewAdmin(FieldsetsInlineMixin, admin.ModelAdmin):
    fieldsets_with_inlines = [
        ('General', {'fields': ['original_recipe', 'batch_name', 'start_date', 'total_quantity']}),
        ('Mashing', {'fields': ['mashing_water_quantity']}),
        BrewMashingIngredientBatchInline,
        ('Brewing', {'fields': ['brew_start_time', 'brew_comments']}),
        BrewBrewingStepInline,
        ('Filtration', {'fields': ['filtration_start_time', 'filtration_water_quantity']}),
        ('Boiling', {'fields': ['boiling_start_time', 'boiling_duration']}),
        BrewBoilingIngredientBatchInline,
        ('Whirlpool', {'fields': ['whirlpool_start_time']}),
        BrewWhirlpoolIngredientBatchInline,
        ('Cooling', {'fields': ['cooling_start_time', 'cooling_end_time']}),
        BrewYeastBatchInline,
        ('Fermentation', {'fields': ['fermentation_tank', 'fermentation_comments']}),
        BrewFermentationStepInline,
        BrewFermentationAnalysisInline,
        BrewAdjunctBatchInline,
    ]
