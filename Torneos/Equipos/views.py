
from typing import List
from django.shortcuts import redirect, render
from Equipos.models import Equipos, Jugadores
from Equipos.forms import RegisterForm, LoginForm, UserEditForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from django.contrib.auth.views import LoginView


def inicio(request):
    return render(request, "inicio.html")


def buscarJugador(request):
    if request.GET:
        nombre = request.GET['nombre']
        jugadores = Jugadores.objects.filter(nombre__icontains=nombre)
        return render(request, "jugadoresBuscar.html", {"jugadores": jugadores, "nombre": nombre})


def buscarEquipo(request):
    if request.GET:
        nombre = request.GET['nombre']
        equipos = Equipos.objects.filter(nombre__icontains=nombre)
        return render(request, "equiposBuscar.html", {"equipos": equipos, "nombre": nombre})


class EquiposList(ListView):

    model = Equipos
    template_name = "equipos.html"


class EquipoDetalle(DetailView):

    model = Equipos
    template_name = "equipo_detalle.html"


class EquipoCreacion(LoginRequiredMixin, CreateView):

    model = Equipos
    success_url = "/equipos/"
    fields = ['nombre', 'nombre_DT', 'abreviatura', 'cant_jugadores', 'escudo', 'torneo_equipo']
    template_name_suffix = '_nuevo'


class EquipoEditar(LoginRequiredMixin, UpdateView):

    model = Equipos
    success_url = "/equipos/"
    fields = ['nombre', 'nombre_DT', 'abreviatura', 'cant_jugadores', 'escudo', 'torneo_equipo']
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

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Usuario creado exitosamente: {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)

            self.request.session.modified = True

        return super(CustomLoginView, self).form_valid(form)

def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect(to='/')

        return super(RegisterView, self).dispatch(request, *args, **kwargs)

def torneos(request):
    return render(request, "Torneos/torneos.html")

def futbol5(request):
    #filtrar solo los equipos que tengan torneo_equipo = futbol5
    equipos = Equipos.objects.filter(torneo_equipo=1)
    return render(request, "Torneos/futbol5.html", {"equipos": equipos})

def futbol8(request):
    equipos = Equipos.objects.filter(torneo_equipo=2)
    return render(request, "Torneos/futbol8.html", {"equipos": equipos})

def futbol11(request):
    equipos = Equipos.objects.filter(torneo_equipo=3)
    return render(request, "Torneos/futbol11.html", {"equipos": equipos})

def construccion(request):
    return render(request, "construccion.html")

def about(request):
    return render(request, "about.html")

@login_required    
def editarPerfil(request):
    
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.username = informacion['username']
            usuario.save()

            return render(request, "inicio.html", {"usuario": usuario})
    else:
        miFormulario = UserEditForm({'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
    return render(request, "editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})