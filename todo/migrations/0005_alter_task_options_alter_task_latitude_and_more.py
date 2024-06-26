# Generated by Django 5.0.6 on 2024-05-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_task_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['status', 'location'], 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterField(
            model_name='task',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='location',
            field=models.CharField(blank=True, choices=[('London,UK', 'London'), ('Berlin,DE', 'Berlin'), ('Paris,FR', 'Paris'), ('Dubai,AE', 'Dubai'), ('Stockholm,SE', 'Stockholm'), ('Wroclaw,PL', 'Wrocław'), ('Current_Loc', 'Get Current Location')], max_length=20, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='task',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='temp',
            field=models.FloatField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='weather',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=''),
        ),
    ]
