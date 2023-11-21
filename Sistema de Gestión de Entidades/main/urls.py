
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('sign-up', views.SignUpView.as_view(), name='sign-up'),
    path('peliculas/', views.peliculas, name="pelicula_list"),
    path('peliculas/<int:pk>', views.pelicula, name="pelicula_details"),
    path('peliculas/crear', views.PeliculaCreate.as_view(), name="pelicula-create"),
    path('peliculas/editar/<int:pk>', views.PeliculaUpdate.as_view(), name="pelicula-edit"),
    path('peliculas/borrar/<int:pk>', views.PeliculaDelete.as_view(), name="pelicula-delete"),
    path('peliculas/sesion/crear', views.SesionCreate.as_view(), name="sesion-create"),
    path('peliculas/sesion/editar/<int:pk>', views.SesionUpdate.as_view(), name="sesion-edit"),
    path('peliculas/sesion/borrar/<int:pk>', views.SesionDelete.as_view(), name="sesion-delete"),
]
