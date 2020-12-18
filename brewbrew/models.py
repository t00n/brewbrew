from django.db import models

class RawMaterial(models.Model):
	variete = models.CharField(max_length=50)


class Producer(models.Model):
	name = models.CharField(max_length=50)


class RawMaterialBatch(models.Model):
	raw_material = models.ForeignKey(RawMaterial)
	producer = models.ForeignKey(Producer)
	batch = models.CharField(max_length=50)
	facture = models.CharField(max_length=50)


class Tank(models.Model):
	name = models.CharField(max_length=50)


class Recipe(models.Model):
	name = models.CharField(max_length=50)
	recipe = models.Text()
	fermentation_time = models.IntegerField()
	fermentation_tank = models.ForeignKey(Tank)
	dry_hopping_time = models.IntegerField()
	dry_hopping_hop1 = models.ForeignKey(RawMaterial)
	dry_hopping_hop2 = models.ForeignKey(RawMaterial)
	dry_hopping_hop3 = models.ForeignKey(RawMaterial)


class RecipeRawMaterial(models.Model):
	raw_material = models.ForeignKey(RawMaterial)
	quantity = models.FloatField()


class Brew(models.Model):
	original_recipe = models.ForeignKey(Recipe)
	name = models.CharField(max_length=50)
	recipe = models.Text()
	fermentation_time = models.IntegerField()
	fermentation_tank = models.ForeignKey(Tank)
	dry_hopping_time = models.IntegerField()
	dry_hopping_hop1 = models.ForeignKey(RawMaterial)
	dry_hopping_hop2 = models.ForeignKey(RawMaterial)
	dry_hopping_hop3 = models.ForeignKey(RawMaterial)


class BrewRawMaterial(models.Model):
	raw_material = models.ForeignKey(RawMaterial)
	quantity = models.FloatField()