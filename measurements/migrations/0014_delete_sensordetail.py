# Generated by Django 4.1.7 on 2023-03-26 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0013_remove_sensordetail_sensor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SensorDetail',
        ),
    ]