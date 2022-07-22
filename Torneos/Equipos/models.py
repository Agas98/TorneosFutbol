
from email.mime import image
from django.db import models
from django.db.models import CharField, ImageField, IntegerField, ForeignKey
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Torneos(models.Model):
    nombre = CharField(max_length=30)
    cantidad_equipos = IntegerField(max_length=30)
    cantidad_jugadores_por_lado = IntegerField(max_length=10)

    def __str__(self):
        return f"{self.nombre}"
class Equipos(models.Model):
    nombre = CharField(max_length=30)
    abreviatura = CharField(max_length=8)
    nombre_DT = CharField(max_length=20)
    cant_jugadores = IntegerField(max_length=35)
    escudo = ImageField(upload_to='Equipos/escudos/', blank=True, null=True)
    torneo_equipo = ForeignKey(Torneos, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} / DT: {self.nombre_DT}"

class PosicionesJugadores(models.Model):
    posicion = CharField(max_length=35)

    def __str__(self):
        return f"{self.posicion}"

class Jugadores(models.Model):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    dorsal = IntegerField(max_length=99)
    equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE)
    posicion = models.ForeignKey(PosicionesJugadores, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido} / Dorsal: {self.dorsal} / {self.equipo.nombre} / {self.posicion}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = ImageField(upload_to='Avatar/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}"

        