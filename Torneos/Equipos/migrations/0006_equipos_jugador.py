# Generated by Django 3.2.13 on 2022-06-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipos', '0005_auto_20220625_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipos',
            name='jugador',
            field=models.ManyToManyField(blank=True, to='Equipos.Jugadores'),
        ),
    ]
