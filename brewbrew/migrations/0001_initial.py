# Generated by Django 3.1.4 on 2020-12-18 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variete', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeRawMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('raw_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbrew.rawmaterial')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('recipe', models.TextField()),
                ('fermentation_time', models.IntegerField()),
                ('dry_hopping_time', models.IntegerField()),
                ('dry_hopping_hop1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_dry_hopping_hop1', to='brewbrew.rawmaterial')),
                ('dry_hopping_hop2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_dry_hopping_hop2', to='brewbrew.rawmaterial')),
                ('dry_hopping_hop3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_dry_hopping_hop3', to='brewbrew.rawmaterial')),
                ('fermentation_tank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbrew.tank')),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterialBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(max_length=50)),
                ('facture', models.CharField(max_length=50)),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbrew.producer')),
                ('raw_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbrew.rawmaterial')),
            ],
        ),
        migrations.CreateModel(
            name='BrewRawMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('raw_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbrew.rawmaterial')),
            ],
        ),
        migrations.CreateModel(
            name='Brew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('recipe', models.TextField()),
                ('fermentation_time', models.IntegerField()),
                ('dry_hopping_time', models.IntegerField()),
                ('dry_hopping_hop1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brew_dry_hopping_hop1', to='brewbrew.rawmaterial')),
                ('dry_hopping_hop2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brew_dry_hopping_hop2', to='brewbrew.rawmaterial')),
                ('dry_hopping_hop3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brew_dry_hopping_hop3', to='brewbrew.rawmaterial')),
                ('fermentation_tank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbrew.tank')),
                ('original_recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbrew.recipe')),
            ],
        ),
    ]