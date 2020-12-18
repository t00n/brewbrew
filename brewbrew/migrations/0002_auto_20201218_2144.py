# Generated by Django 3.1.4 on 2020-12-18 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brewbrew', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='fermentation_tank',
        ),
        migrations.AddField(
            model_name='brew',
            name='dry_hopping_hop1_quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='brew',
            name='dry_hopping_hop2_quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='brew',
            name='dry_hopping_hop3_quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='dry_hopping_hop1_quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='dry_hopping_hop2_quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='dry_hopping_hop3_quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='brew',
            name='dry_hopping_hop1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brew_dry_hopping_hop1', to='brewbrew.rawmaterial'),
        ),
        migrations.AlterField(
            model_name='brew',
            name='dry_hopping_hop2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brew_dry_hopping_hop2', to='brewbrew.rawmaterial'),
        ),
        migrations.AlterField(
            model_name='brew',
            name='dry_hopping_hop3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brew_dry_hopping_hop3', to='brewbrew.rawmaterial'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='dry_hopping_hop1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_dry_hopping_hop1', to='brewbrew.rawmaterial'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='dry_hopping_hop2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_dry_hopping_hop2', to='brewbrew.rawmaterial'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='dry_hopping_hop3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_dry_hopping_hop3', to='brewbrew.rawmaterial'),
        ),
    ]
