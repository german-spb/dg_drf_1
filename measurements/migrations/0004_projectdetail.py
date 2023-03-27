# Generated by Django 4.1.7 on 2023-03-25 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0003_measurement'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurements.project')),
            ],
        ),
    ]