# Generated by Django 3.1.4 on 2020-12-20 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brewbrew', '0006_auto_20201220_1306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeboilingingredient',
            old_name='boiling_ingredient',
            new_name='ingredient',
        ),
        migrations.RenameField(
            model_name='recipemashingingredient',
            old_name='mashing_ingredient',
            new_name='ingredient',
        ),
        migrations.RenameField(
            model_name='recipewhirlpoolingredient',
            old_name='whirlpool_ingredient',
            new_name='ingredient',
        ),
    ]