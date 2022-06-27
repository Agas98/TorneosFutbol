from django.urls import path

from Equipos import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('equipos/cargarEquipos/', views.formularioEquipos, name="formularioEquipos"),
    path('equipos/buscarEquipo/', views.buscarEquipo, name="buscarEquipo"),
    path('jugadores/', views.jugadores, name="Jugadores"),
    path('jugadores/cargarJugadores/', views.formularioJugadores, name="formularioJugadores"),
    path('jugadores/buscarJugador/', views.buscarJugador, name="buscarJugador"),

    path('equipos/', views.EquiposList.as_view(), name='Equipos'),
    path('equipos/'r'^(?P<pk>\d+)$', views.EquipoDetalle.as_view(), name='Detalle'),
    path(r'^nuevo$', views.EquipoCreacion.as_view(), name='Nuevo'),
    path(r'^editar/(?P<pk>\d+)$', views.EquipoEditar.as_view(), name='Editar'),
    path(r'^borrar/(?P<pk>\d+)$', views.EquipoEliminar.as_view(), name='Eliminar'),
]