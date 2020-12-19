from django.db import models

class RawMaterial(models.Model):
    variete = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.variete


class Producer(models.Model):
    name = models.CharField(max_length=50)


class RawMaterialBatch(models.Model):
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    batch = models.CharField(max_length=50)
    facture = models.CharField(max_length=50)
    quantity = models.FloatField()


class Tank(models.Model):
    name = models.CharField(max_length=50)


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.TextField()
    fermentation_time = models.IntegerField()
    dry_hopping_time = models.IntegerField()
    dry_hopping_hop1 = models.ForeignKey(RawMaterial, null=True, blank=True, on_delete=models.CASCADE, related_name='recipe_dry_hopping_hop1')
    dry_hopping_hop1_quantity = models.FloatField(null=True, blank=True)
    dry_hopping_hop2 = models.ForeignKey(RawMaterial, null=True, blank=True, on_delete=models.CASCADE, related_name='recipe_dry_hopping_hop2')
    dry_hopping_hop2_quantity = models.FloatField(null=True, blank=True)
    dry_hopping_hop3 = models.ForeignKey(RawMaterial, null=True, blank=True, on_delete=models.CASCADE, related_name='recipe_dry_hopping_hop3')
    dry_hopping_hop3_quantity = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class RecipeRawMaterial(models.Model):
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity = models.FloatField()


class Brew(models.Model):
    original_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    recipe = models.TextField()
    fermentation_time = models.IntegerField()
    fermentation_tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    dry_hopping_time = models.IntegerField()
    dry_hopping_hop1 = models.ForeignKey(RawMaterial, null=True, blank=True, on_delete=models.CASCADE, related_name='brew_dry_hopping_hop1')
    dry_hopping_hop1_quantity = models.FloatField(null=True, blank=True)
    dry_hopping_hop2 = models.ForeignKey(RawMaterial, null=True, blank=True, on_delete=models.CASCADE, related_name='brew_dry_hopping_hop2')
    dry_hopping_hop2_quantity = models.FloatField(null=True, blank=True)
    dry_hopping_hop3 = models.ForeignKey(RawMaterial, null=True, blank=True, on_delete=models.CASCADE, related_name='brew_dry_hopping_hop3')
    dry_hopping_hop3_quantity = models.FloatField(null=True, blank=True)


class BrewRawMaterial(models.Model):
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity = models.FloatField()