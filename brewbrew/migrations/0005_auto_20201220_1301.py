# Generated by Django 3.1.4 on 2020-12-20 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brewbrew', '0004_merge_20201220_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brew',
            name='dry_hopping_hop1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='brew_dry_hopping_hop1', to='brewbrew.ingredient'),
        ),
        migrations.AlterField(
            model_name='brew',
            name='dry_hopping_hop2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='brew_dry_hopping_hop2', to='brewbrew.ingredient'),
        ),
        migrations.AlterField(
            model_name='brew',
            name='dry_hopping_hop3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='brew_dry_hopping_hop3', to='brewbrew.ingredient'),
        ),
        migrations.AlterField(
            model_name='brew',
            name='fermentation_tank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='brewbrew.tank'),
        ),
        migrations.AlterField(
            model_name='brew',
            name='original_recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='brewbrew.recipe'),
        ),
    ]