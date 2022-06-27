# Generated by Django 3.2.13 on 2022-06-27 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Equipos', '0007_auto_20220627_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipos',
            name='jugador',
        ),
        migrations.AddField(
            model_name='equipos',
            name='torneo_equipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Equipos.torneos'),
        ),
    ]
