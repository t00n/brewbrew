# Generated by Django 3.1.4 on 2020-12-19 12:46

from django.db import migrations, models
import django.db.models.deletion

from datetime import timedelta

class Migration(migrations.Migration):

    dependencies = [
        ('brewbrew', '0003_auto_20201219_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrewingStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(help_text='Temperature during this brewing step')),
                ('duration', models.IntegerField(help_text='Duration of this brewing step in minutes')),
            ],
        ),
        migrations.CreateModel(
            name='FermentationStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(help_text='Temperature during this fermentation step')),
                ('duration', models.IntegerField(help_text='Duration of this fermentation step in days')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variety', models.CharField(help_text='Name/variety of the ingredient', max_length=50)),
                ('unit', models.CharField(help_text='Unit of measure of the ingredient', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.CharField(help_text='Batch number', max_length=50)),
                ('bill_number', models.CharField(help_text='Bill number', max_length=50)),
                ('quantity', models.FloatField(help_text='Quantity in the batch')),
                ('ingredient', models.ForeignKey(help_text='Ingredient', on_delete=django.db.models.deletion.RESTRICT, to='brewbrew.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeAdjuncts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(help_text='Quantity to use in the recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeBoilingIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(help_text='Quantity to use in the recipe')),
                ('time', models.IntegerField(help_text='When to add the ingredient (in minutes from the end of boiling)')),
                ('boiling_ingredient', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='brewbrew.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeMashingIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(help_text='Quantity to use in the recipe')),
                ('mashing_ingredient', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='brewbrew.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeWhirlpoolIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(help_text='Quantity to use in the recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeYeasts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(help_text='Quantity to use in the recipe')),
            ],
        ),
        migrations.RemoveField(
            model_name='rawmaterialbatch',
            name='producer',
        ),
        migrations.RemoveField(
            model_name='rawmaterialbatch',
            name='raw_material',
        ),
        migrations.RemoveField(
            model_name='reciperawmaterial',
            name='raw_material',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='dry_hopping_hop1',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='dry_hopping_hop1_quantity',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='dry_hopping_hop2',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='dry_hopping_hop2_quantity',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='dry_hopping_hop3',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='dry_hopping_hop3_quantity',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='dry_hopping_time',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='fermentation_time',
        ),
        migrations.AddField(
            model_name='recipe',
            name='boiling_duration',
            field=models.DurationField(default=timedelta(0), help_text='Duration of boiling step'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='filtration_water_quantity',
            field=models.FloatField(default=0, help_text='Liters of waters to add during filtration'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='mashing_water_quantity',
            field=models.FloatField(default=0, help_text='Liters of water to add during mashing'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(help_text='Name of the recipe', max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe',
            field=models.TextField(help_text='Written description of the recipe'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(help_text='Name of the supplier', max_length=50),
        ),
        migrations.AlterField(
            model_name='tank',
            name='name',
            field=models.CharField(help_text='Name/number of the tank', max_length=50),
        ),
        migrations.DeleteModel(
            name='BrewRawMaterial',
        ),
        migrations.DeleteModel(
            name='RawMaterialBatch',
        ),
        migrations.DeleteModel(
            name='RecipeRawMaterial',
        ),
        migrations.AddField(
            model_name='recipeyeasts',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbrew.recipe'),
        ),
        migrations.AddField(
            model_name='recipeyeasts',
            name='yeast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='brewbrew.ingredient'),
        ),
        migrations.AddField(
            model_name='recipewhirlpoolingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbrew.recipe'),
        ),
        migrations.AddField(
            model_name='recipewhirlpoolingredient',
            name='whirlpool_ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='brewbrew.ingredient'),
        ),
        migrations.AddField(
            model_name='recipemashingingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbrew.recipe'),
        ),
        migrations.AddField(
            model_name='recipeboilingingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbrew.recipe'),
        ),
        migrations.AddField(
            model_name='recipeadjuncts',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbrew.recipe'),
        ),
        migrations.AddField(
            model_name='recipeadjuncts',
            name='yeast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='brewbrew.ingredient'),
        ),
        migrations.AddField(
            model_name='ingredientbatch',
            name='producer',
            field=models.ForeignKey(help_text='Supplier', on_delete=django.db.models.deletion.RESTRICT, to='brewbrew.supplier'),
        ),
        migrations.AddField(
            model_name='fermentationstep',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbrew.recipe'),
        ),
        migrations.AddField(
            model_name='brewingstep',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbrew.recipe'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='adjuncts',
            field=models.ManyToManyField(help_text='Adjuncts/Hops to add during fermentation', related_name='recipe_adjuncts', through='brewbrew.RecipeAdjuncts', to='brewbrew.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='boiling_ingredients',
            field=models.ManyToManyField(help_text='Ingredients to add during boiling', related_name='recipe_boiling', through='brewbrew.RecipeBoilingIngredient', to='brewbrew.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='mashing_ingredients',
            field=models.ManyToManyField(help_text='Ingredients to add during mashing', related_name='recipe_mashing', through='brewbrew.RecipeMashingIngredient', to='brewbrew.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='whirlpool_ingredients',
            field=models.ManyToManyField(help_text='Ingredients to add during whirlpool', related_name='recipe_whirlpool', through='brewbrew.RecipeWhirlpoolIngredient', to='brewbrew.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='yeasts',
            field=models.ManyToManyField(help_text='Yeasts to add before fermentation', related_name='recipe_yeasts', through='brewbrew.RecipeYeasts', to='brewbrew.Ingredient'),
        ),
        migrations.AlterField(
            model_name='brew',
            name='dry_hopping_hop1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brew_dry_hopping_hop1', to='brewbrew.ingredient'),
        ),
        migrations.AlterField(
            model_name='brew',
            name='dry_hopping_hop2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brew_dry_hopping_hop2', to='brewbrew.ingredient'),
        ),
        migrations.AlterField(
            model_name='brew',
            name='dry_hopping_hop3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brew_dry_hopping_hop3', to='brewbrew.ingredient'),
        ),
        migrations.DeleteModel(
            name='RawMaterial',
        ),
    ]