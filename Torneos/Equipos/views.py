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


def inicio(request):

    return render(request, "inicio.html")

def formularioEquipos(request):

    if request.method == 'POST':

        equipoFormulario = EquiposFormulario(request.POST, request.FILES)

        if equipoFormulario.is_valid:

            equipo = Equipos(nombre=request.POST['nombre'], nombre_DT=request.POST['nombre_DT'], abreviatura=request.POST['abreviatura'], cant_jugadores=request.POST['cant_jugadores'], escudo=request.FILES['escudo'])

            equipo.save()

            return redirect("/equipos/")

    else:

        equipoFormulario = EquiposFormulario()

    return render(request, "formularioEquipos.html", {"equipoFormulario": equipoFormulario})

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
    success_url = "/equipos/list"
    fields  = ['nombre', 'nombre_DT', 'abreviatura', 'cant_jugadores', 'escudo']

class EquipoEditar(UpdateView):

    model = Equipos
    success_url = "/equipos/list"
    fields  = ['nombre', 'nombre_DT', 'abreviatura', 'cant_jugadores', 'escudo']

class EquipoEliminar(DeleteView):

    model = Equipos
    success_url = "/equipos/list"