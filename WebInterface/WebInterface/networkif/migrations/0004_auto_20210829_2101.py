# Generated by Django 3.2.6 on 2021-08-30 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networkif', '0003_networkif_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networkif',
            name='sensorReadings',
        ),
        migrations.AddField(
            model_name='networkif',
            name='sensorData',
            field=models.JSONField(blank=True, default={}),
        ),
        migrations.AlterField(
            model_name='networkif',
            name='timestamp',
            field=models.JSONField(blank=True, default={}),
        ),
    ]
