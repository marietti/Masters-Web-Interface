# Generated by Django 3.2.6 on 2021-09-07 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0003_auto_20210904_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interface',
            name='sensorCounts',
        ),
        migrations.AddField(
            model_name='interface',
            name='changepoint',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interface',
            name='sensorData',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='interface',
            name='timestamp',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
