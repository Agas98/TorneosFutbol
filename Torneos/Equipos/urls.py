from re import template
from django.urls import path

from Equipos import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('jugadores/', views.jugadores, name="Jugadores"),
    path('jugadores/cargarJugadores/', views.formularioJugadores, name="formularioJugadores"),
    path('jugadores/buscarJugador/', views.buscarJugador, name="buscarJugador"),

    path('equipos/', views.EquiposList.as_view(), name='Equipos'),
    path('equipos/buscarEquipo/', views.buscarEquipo, name="buscarEquipo"),
    path('equipos/'r'^(?P<pk>\d+)$', views.EquipoDetalle.as_view(), name='DetalleEquipo'),
    path('equiposEditar/'r'^(?P<pk>\d+)$', views.EquipoEditar.as_view(), name='EditarEquipo'),
    path('equiposBorrar/'r'^(?P<pk>\d+)$', views.EquipoEliminar.as_view(), name='EliminarEquipo'),
    path('equiposNuevo/', views.EquipoCreacion.as_view(), name='NuevoEquipo'),

    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Registro"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="Logout"),
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