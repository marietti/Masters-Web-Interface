# Generated by Django 3.1.6 on 2021-02-26 03:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changepoint', '0013_auto_20210225_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changepoint',
            name='sensorCounts',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=2), size=2),
        ),
    ]
