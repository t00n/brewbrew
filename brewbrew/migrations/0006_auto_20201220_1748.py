# Generated by Django 3.1.4 on 2020-12-20 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brewbrew', '0005_auto_20201220_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewmashingingredientbatch',
            name='ingredient_batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='brewbrew.ingredientbatch'),
        ),
    ]
