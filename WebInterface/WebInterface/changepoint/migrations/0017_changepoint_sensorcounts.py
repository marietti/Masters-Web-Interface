# Generated by Django 3.1.6 on 2021-02-26 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changepoint', '0016_remove_changepoint_sensorcounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='changepoint',
            name='sensorCounts',
            field=models.JSONField(null=True),
        ),
    ]
