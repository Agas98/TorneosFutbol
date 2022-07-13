from re import template
from django.shortcuts import redirect
from django.urls import path, include

from Equipos import views
from .views import RegisterView, CustomLoginView, ResetPasswordView
from .forms import LoginForm
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('jugadores/buscarJugador/', views.buscarJugador, name="buscarJugador"),

    path('equipos/', views.EquiposList.as_view(), name='Equipos'),
    path('equipos/buscarEquipo/', views.buscarEquipo, name="buscarEquipo"),
    path('equipos/'r'^(?P<pk>\d+)$', views.EquipoDetalle.as_view(), name='DetalleEquipo'),
    path('equiposEditar/'r'^(?P<pk>\d+)$', views.EquipoEditar.as_view(), name='EditarEquipo'),
    path('equiposBorrar/'r'^(?P<pk>\d+)$', views.EquipoEliminar.as_view(), name='EliminarEquipo'),
    path('equiposNuevo/', views.EquipoCreacion.as_view(), name='NuevoEquipo'),

    path('jugadores/', views.JugadoresList.as_view(), name='Jugadores'),
    path('jugadoresNuevo/', views.JugadorCreacion.as_view(), name='NuevoJugador'),
    path('jugadoresEditar/'r'^(?P<pk>\d+)$', views.JugadorEditar.as_view(), name='EditarJugador'),
    path('jugadoresBorrar/'r'^(?P<pk>\d+)$', views.JugadorEliminar.as_view(), name='EliminarJugador'),

    path('torneos/', views.torneos, name="Torneos"),

    path("__reload__/", include("django_browser_reload.urls")),

    path('registro/', RegisterView.as_view(), name="Registro"),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html', authentication_form=LoginForm), name="Login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="Logout"),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

    url(r'^oauth/', include('social_django.urls', namespace='social')),
]

# ACLARACIÓN IMPORTANTE!!!!!!!
# path(r'^(?P<pk>\d+)$'
# Es una expresión regular, que se compara con la URL real.
# Aquí r'' especifica que la cadena es una cadena sin procesar.
# '^' significa el comienzo y $ marca el final.
# Ahora 'pk' (cuando está dentro de <>) representa una clave principal.
# Una clave principal puede ser cualquier cosa, por ejemplo.
# puede ser una cadena, un número, etc.
# Una clave principal se usa para diferenciar diferentes columnas
# de una tabla. aqui esta escrito.
#<pk>\d+ \d coincide con [0-9] y otros caracteres de dígitos.
#'+' significa que debe haber al menos 1 o más dígitos en el número.