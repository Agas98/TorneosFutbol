from multiprocessing import AuthenticationError
from typing import List
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from Equipos.models import Equipos, Jugadores, PosicionesJugadores, Torneos, Avatar, User
from Equipos.forms import RegisterForm, LoginForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


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

def torneos(request):
    return render(request, "torneos.html")

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
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                    "if an account exists with the email you entered. You should receive them shortly." \
                    " If you don't receive an email, " \
                    "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('Login')