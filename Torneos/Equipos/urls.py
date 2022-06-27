from django.urls import path

from Equipos import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('equipos/', views.equipos, name="Equipos"),
    path('equipos/cargarEquipos/', views.formularioEquipos, name="formularioEquipos"),
    path('equipos/buscarEquipo/', views.buscarEquipo, name="buscarEquipo"),
    path('jugadores/', views.jugadores, name="Jugadores"),
    path('jugadores/cargarJugadores/', views.formularioJugadores, name="formularioJugadores"),
    path('jugadores/buscarJugador/', views.buscarJugador, name="buscarJugador"),
]