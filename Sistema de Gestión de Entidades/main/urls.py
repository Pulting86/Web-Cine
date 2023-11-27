
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name="index"),
    path('sign-up', views.SignUpView.as_view(), name='sign-up'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="restablecer_contraseña"),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name='password_reset_complete'),
    path('peliculas/', views.peliculas, name="pelicula_list"),
    path('peliculas/<int:pk>', views.pelicula, name="pelicula_details"),
    path('peliculas/crear', views.PeliculaCreate.as_view(), name="pelicula-create"),
    path('peliculas/editar/<int:pk>', views.PeliculaUpdate.as_view(), name="pelicula-edit"),
    path('peliculas/borrar/<int:pk>', views.PeliculaDelete.as_view(), name="pelicula-delete"),
    path('peliculas/sesion/crear', views.SesionCreate.as_view(), name="sesion-create"),
    path('peliculas/sesion/editar/<int:pk>', views.SesionUpdate.as_view(), name="sesion-edit"),
    path('peliculas/sesion/borrar/<int:pk>', views.SesionDelete.as_view(), name="sesion-delete"),
    path('sala/reservar/<int:pk>', views.reservar, name="reservar"),
    path('sala/vaciar/<int:pk>', views.vaciar, name="vaciar-sala"),
    path('buscar/', views.buscar, name='buscar'),
]
