from multiprocessing import AuthenticationError
from typing import List
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from Equipos.models import Equipos, Jugadores, PosicionesJugadores, Torneos, Avatar,User
from Equipos.forms import EquiposFormulario, JugadoresFormulario, UserRegisterForm, UserEditForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required


@login_required
def inicio(request):

    if request.user.is_authenticated:
        avatares = Avatar.objects.get(user=request.user)
        return render(request, "inicio.html", {"avatar": avatares.imagen.url})
    return render(request, "inicio.html")

def buscarJugador(request):
    if request.GET:
        nombre = request.GET['nombre']
        buscador = 1  # para activar el boton "Volver"
        jugadores = Jugadores.objects.filter(nombre__icontains=nombre)
        return render(request, "jugadoresBuscar.html", {"jugadores": jugadores, "buscador": buscador, "nombre": nombre})


def buscarEquipo(request):

    if request.GET:
        nombre = request.GET['nombre']
        buscador = 1  # para activar el boton "Volver"
        equipos = Equipos.objects.filter(nombre__icontains=nombre)
        return render(request, "equiposBuscar.html", {"equipos": equipos, "buscador": buscador, "nombre": nombre})


class EquiposList(ListView):

    model = Equipos
    template_name = "equipos.html"


class EquipoDetalle(DetailView):

    model = Equipos
    template_name = "equipo_detalle.html"


class EquipoCreacion(LoginRequiredMixin, CreateView):

    model = Equipos
    success_url = "/equipos/"
    fields = ['nombre', 'nombre_DT', 'abreviatura',
              'cant_jugadores', 'escudo', 'torneo_equipo']
    template_name_suffix = '_nuevo'


class EquipoEditar(LoginRequiredMixin, UpdateView):

    model = Equipos
    success_url = "/equipos/"
    fields = ['nombre', 'nombre_DT', 'abreviatura',
              'cant_jugadores', 'escudo', 'torneo_equipo']
    template_name_suffix = '_actualizar'


class EquipoEliminar(LoginRequiredMixin, DeleteView):

    model = Equipos
    success_url = "/equipos/"
    template_name_suffix = '_eliminar'


class JugadoresList(ListView):

    model = Jugadores
    template_name = "jugadores.html"


class JugadorCreacion(LoginRequiredMixin, CreateView):

    model = Jugadores
    success_url = "/jugadores/"
    fields = ['nombre', 'apellido', 'dorsal', 'equipo', 'posicion']
    template_name_suffix = '_nuevo'


class JugadorEditar(LoginRequiredMixin, UpdateView):

    model = Jugadores
    success_url = "/jugadores/"
    fields = ['nombre', 'apellido', 'dorsal', 'equipo', 'posicion']
    template_name_suffix = '_actualizar'


class JugadorEliminar(LoginRequiredMixin, DeleteView):

    model = Jugadores
    success_url = "/jugadores/"
    template_name_suffix = '_eliminar'


class JugadoresEquipo(ListView):

    model = Jugadores
    template_name = "equipo_detalle_jugadores.html"


def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)

                return redirect('/', {"mensaje": "Usuario autenticado correctamente"})

            else:

                return render(request, "login.html", {"mensaje": "Usuario o contraseña incorrectos"})

        else:
            return render(request, "login.html", {"mensaje": "Usuario o contraseña incorrectos"})

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('/login/', {"mensaje": "Usuario creado correctamente"})
    else:

        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})


def logout(request):
    return render(request, "logout.html")


@login_required
def editarPerfil(request):
    #se instancia el Login;
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():  # si pasa la validación Django
            informacion = miFormulario.cleaned_data

            #datos que modificaríamos
            usuario.email = informacion['email']  # alg@algo.com
            usuario.password1 = informacion['password1']  # pass
            usuario.password2 = informacion['password2']
            usuario.avatar = informacion['avatar']
            usuario.save()

            return render(request, "inicio.html",{"mensaje": "Usuario editado correctamente"})

    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})

