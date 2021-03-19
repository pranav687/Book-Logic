# Generated by Django 3.1.5 on 2021-03-16 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_flights_arrival_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flights',
            name='available_seats',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='flights',
            name='departure_date',
            field=models.DateField(default=datetime.date(2021, 3, 16)),
        ),
        migrations.AlterField(
            model_name='flights',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='num_seats',
            field=models.IntegerField(),
        ),
    ]
