# Generated by Django 3.2.6 on 2021-09-07 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0005_interface_sensorcounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='interface',
            name='sensorCountsChangePoint',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
