# Generated by Django 3.1.4 on 2020-12-22 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewbrew', '0012_ingredientbatchinput_input_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientbatchinput',
            name='input_time',
            field=models.DateTimeField(),
        ),
    ]
