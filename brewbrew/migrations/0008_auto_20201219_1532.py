# Generated by Django 3.1.4 on 2020-12-19 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brewbrew', '0007_auto_20201219_1532'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipeAdjuncts',
            new_name='RecipeAdjunct',
        ),
    ]