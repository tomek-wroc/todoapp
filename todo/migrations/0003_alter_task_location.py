# Generated by Django 5.0.6 on 2024-05-20 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_temp_task_weather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='location',
            field=models.CharField(blank=True, choices=[('London,UK', 'London'), ('Berlin,DE', 'Berlin'), ('Paris,FR', 'Paris'), ('Dubai,AE', 'Dubai'), ('Stockholm,SE', 'Stockholm'), ('Wroclaw,PL', 'Wrocław')], max_length=20, null=True, verbose_name='Location'),
        ),
    ]
