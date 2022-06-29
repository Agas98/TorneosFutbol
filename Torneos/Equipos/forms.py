from django import forms
from Equipos.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EquiposFormulario(forms.Form):   
    nombre = forms.CharField(max_length=30)
    abreviatura = forms.CharField(max_length=8)
    nombre_DT = forms.CharField(max_length=20)
    cant_jugadores = forms.IntegerField(max_value=35)
    escudo = forms.ImageField(required=False)
    torneo_equipo = forms.ModelChoiceField(Torneos.objects.all())

class JugadoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dorsal = forms.IntegerField(max_value=99)
    equipo = forms.ModelChoiceField(queryset=Equipos.objects.all())
    posicion = forms.ModelChoiceField(queryset=PosicionesJugadores.objects.all())

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}