from audioop import reverse
from datetime import *
from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .form import SignUpForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
from django.http import Http404

# Create your views here.

def index(request):
    peliculas = Pelicula.objects.all()
    sesion = Sesion.objects.all()
    sala = Sala.objects.all()

    context = {
        'pelicula': peliculas,
        'sesion': sesion,
        'sala': sala,
    }

    return render(request, 'index.html', context)


def peliculas(request):
    peliculas = Pelicula.objects.all()

    context = {
        'peliculas': peliculas,
    }

    return render(request, 'pelicula_list.html', context)


def pelicula(request, pk):
    pelicula = Pelicula.objects.get(pk=pk)
    api = API_Pelicula.objects.get(pk=pk)
    copias = Copia.objects.all()
    copias_pelicula = []

    for copia in copias:
        if copia.pelicula.pk == pk:
            copias_pelicula.append(copia)

    context = {
        'pelicula': pelicula,
        'api': api,
        'copias': copias_pelicula,
    }

    return render(request, 'pelicula_details.html', context)


class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')


class PeliculaCreate(LoginRequiredMixin, CreateView):
    model = Pelicula
    fields = '__all__'

class PeliculaUpdate(LoginRequiredMixin, UpdateView):
    model = Pelicula
    fields = '__all__'

class PeliculaDelete(LoginRequiredMixin, DeleteView):
    model = Pelicula
    success_url = reverse_lazy('peliculas_list')

class SesionCreate(LoginRequiredMixin, CreateView):
    model = Copia
    fields = '__all__'

class SesionUpdate(LoginRequiredMixin, UpdateView):
    model = Copia
    fields = '__all__'

class SesionDelete(LoginRequiredMixin, DeleteView):
    model = Copia
    success_url = reverse_lazy('peliculas_details')

class APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return API_Pelicula.objects.get(pk=pk)
        except API_Pelicula.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = APISerializers(post)
        return Response(serializer.data)
