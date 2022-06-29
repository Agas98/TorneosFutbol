from multiprocessing import AuthenticationError
from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from Equipos.models import Equipos, Jugadores, PosicionesJugadores
from Equipos.forms import EquiposFormulario, JugadoresFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):

    return render(request, "inicio.html")

def formularioJugadores(request):

    if request.method == 'POST':

        jugadorFormulario = JugadoresFormulario(request.POST, request.FILES)

        if jugadorFormulario.is_valid:

            jugador = Jugadores(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            dorsal=request.POST['dorsal'],
            equipo=Equipos.objects.get(id=request.POST['equipo']),
            posicion=PosicionesJugadores.objects.get(id=request.POST['posicion']))

            jugador.save()

            return redirect("/jugadores/")

    else:

        jugadorFormulario = JugadoresFormulario()

    return render(request, "formularioJugadores.html", {"jugadorFormulario": jugadorFormulario})

def jugadores(request):
    return render(request, "jugadores.html", {"jugadores": Jugadores.objects.all()})

def buscarJugador(request):
    if request.GET:
        nombre = request.GET['nombre']
        buscador = 1    #para activar el boton "Volver"
        jugadores = Jugadores.objects.filter(nombre__icontains=nombre)
        return render(request, "jugadores.html", {"jugadores": jugadores, "buscador": buscador, "nombre": nombre})

def buscarEquipo(request):

    if request.GET:
        nombre = request.GET['nombre']
        buscador = 1    #para activar el boton "Volver"
        equipos = Equipos.objects.filter(nombre__icontains=nombre)
        return render(request, "equiposBuscar.html", {"equipos": equipos, "buscador": buscador, "nombre": nombre})


class EquiposList(ListView):

    model = Equipos 
    template_name = "equipos.html"

class EquipoDetalle(DetailView):

    model = Equipos
    template_name = "equipo_detalle.html"

class EquipoCreacion(CreateView):

    model = Equipos
    success_url = "/equipos/"
    fields  = ['nombre', 'nombre_DT', 'abreviatura', 'cant_jugadores', 'escudo', 'torneo_equipo']
    template_name_suffix = '_nuevo'

class EquipoEditar(UpdateView):

    model = Equipos
    success_url = "/equipos/"
    fields  = ['nombre', 'nombre_DT', 'abreviatura', 'cant_jugadores', 'escudo', 'torneo_equipo']
    template_name_suffix = '_actualizar'

class EquipoEliminar(DeleteView):

    model = Equipos
    success_url = "/equipos/"
    template_name_suffix = '_eliminar'

def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                
                login(request, user)

                return render(request, "inicio.html", {"mensaje": "Bienvenido " + username})

            else:

                return render(request, "login.html", {"mensaje": "Usuario o contraseña incorrectos"})
        
        else:
            return render(request, "login.html", {"mensaje": "Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect("/login/")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})

def logout(request):
    return render(request, "logout.html")