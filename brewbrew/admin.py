from django.contrib import admin
from .models import (
    RawMaterial,
    Recipe,
)


class RawMaterialAdmin(admin.ModelAdmin):
    pass


class RecipeAdmin(admin.ModelAdmin):
    pass


admin.site.register(RawMaterial, RawMaterialAdmin)
admin.site.register(Recipe, RecipeAdmin)
