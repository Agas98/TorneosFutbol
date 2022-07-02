from cProfile import label
from tkinter import Widget
from turtle import width
from django import forms
from Equipos.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EquiposFormulario(forms.Form):   
    nombre = forms.CharField(max_length=30)
    abreviatura = forms.CharField(max_length=8)
    nombre_DT = forms.CharField(label='Nombre completo DT',max_length=20)
    cant_jugadores = forms.IntegerField(label='Cantidad de jugadores',max_value=35)
    escudo = forms.ImageField(required=False)
    torneo_equipo = forms.ModelChoiceField(Torneos.objects.all())

class JugadoresFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre',max_length=30)
    apellido = forms.CharField(label='Apellido',max_length=30)
    dorsal = forms.IntegerField(label='Dorsal',max_value=99)
    equipo = forms.ModelChoiceField(label='Equipo',queryset=Equipos.objects.all())
    posicion = forms.ModelChoiceField(label='Posicion',queryset=PosicionesJugadores.objects.all())

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

#La clase meta es una clase interna en los modelos de Django.
#Que contienen opciones Meta (metadatos) que se utilizan para
#cambiar el comportamiento de los campos de su modelo,
#como cambiar las opciones de orden, si el modelo es abstracto o no,
#versiones singulares y plurales del nombre, etc. 

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita la contraseña', widget=forms.PasswordInput)
    avatar = forms.ImageField(label='Avatar', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'avatar']
        help_texts = {k:"" for k in fields}




#class models.User
# User objects have the following fields:

# username¶
# Required. 150 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.

# The max_length should be sufficient for many use cases. If you need a longer length, please use a custom user model. If you use MySQL with the utf8mb4 encoding (recommended for proper Unicode support), specify at most max_length=191 because MySQL can only create unique indexes with 191 characters in that case by default.

# first_name¶
# Optional (blank=True). 150 characters or fewer.

# last_name¶
# Optional (blank=True). 150 characters or fewer.

# email¶
# Optional (blank=True). Email address.

# password¶
# Required. A hash of, and metadata about, the password. (Django doesn’t store the raw password.) Raw passwords can be arbitrarily long and can contain any character. See the password documentation.

# groups¶
# Many-to-many relationship to Group