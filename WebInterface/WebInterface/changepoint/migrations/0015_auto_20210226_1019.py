# Generated by Django 3.1.6 on 2021-02-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changepoint', '0014_auto_20210225_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changepoint',
            name='sensorCounts',
            field=models.JSONField(null=True),
        ),
    ]
