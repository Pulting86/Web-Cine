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
from django.contrib.auth import views as auth_views

# Create your views here.

def index(request):
    peliculas = Pelicula.objects.all()
    sesion = Sesion.objects.all()
    sala = Sala.objects.all()
    api = list(API_Pelicula.objects.all())
    api_1 = api[0]
    api.remove(api[0])

    context = {
        'pelicula': peliculas,
        'sesion': sesion,
        'sala': sala,
        'api': api,
        'api_1': api_1,
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
    apis = API_Pelicula.objects.all()
    api_pelicula = []

    for api in apis:
        if api.pelicula_id.pk == pk:
            api_pelicula.append(api)

    copias = Copia.objects.all()
    copias_pelicula = []

    for copia in copias:
        if copia.pelicula.pk == pk:
            copias_pelicula.append(copia)

    context = {
        'pelicula': pelicula,
        'apis': api_pelicula,
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

def zip_listas(lista1, lista2):
    return zip(lista1, lista2)

def buscar(request):
    peliculas = []

    if 'q' in request.GET:
        query = request.GET['q']
        objetos_resultado = Pelicula.objects.filter(titulo__icontains=query)

        if 'filtrar' in request.GET and request.GET['filtrar'] == 'Acción':

            objetos_resultado = objetos_resultado.filter(categorias__exact='Acción')

        if 'filtrar' in request.GET and request.GET['filtrar'] == 'Romántica':

            objetos_resultado = objetos_resultado.filter(categorias__exact='Romántica')

        if 'filtrar' in request.GET and request.GET['filtrar'] == 'Animación':

            objetos_resultado = objetos_resultado.filter(categorias__exact='Animación')

        if 'filtrar' in request.GET and request.GET['filtrar'] == 'Terror':

            objetos_resultado = objetos_resultado.filter(categorias__exact='Terror')

        if 'filtrar' in request.GET and request.GET['filtrar'] == 'Ciencia ficción':

            objetos_resultado = objetos_resultado.filter(categorias__exact='Ciencia ficción')

        resultados = list(objetos_resultado.values())

        if resultados:
            for resultado in resultados:
                pelicula = Pelicula.objects.get(id=resultado['id'])
                peliculas.append(pelicula)

    else:
        resultados = Pelicula.objects.all()
        for resultado in resultados:
            peliculas.append(resultado)

    context = {
        'resultados': resultados,
        'peliculas': peliculas,
        'zip_listas': zip_listas(resultados, peliculas)
    }

    return render(request, 'buscar.html', context)

def reservar(request,pk):
    sala = Sala.objects.get(pk=pk)
    peliculas = Pelicula.objects.all()


    if request.method == 'POST':
        for i in range(1 + 50 * (sala.id - 1), 51 + 50 * (sala.id - 1)):
            checkbox = request.POST.get('asiento_' + str(i))
            if checkbox:
                asiento = Asiento.objects.get(pk=i)
                asiento.cliente = request.user
                asiento.reservado = True

                asiento.save()

        context = {
            'peliculas':peliculas,
        }

        return render(request, 'pelicula_list.html', context)

    context = {
        'sala': sala,
    }
    return render(request, 'reservar.html', context)



def vaciar(request,pk):
    sala = Sala.objects.get(pk=pk)
    peliculas = Pelicula.objects.all()

    for i in range(1 + 50 * (sala.id - 1), 51 + 50 * (sala.id - 1)):
        asiento = Asiento.objects.get(pk=i)
        asiento.cliente = None
        asiento.reservado = False

        asiento.save()

    context = {
        'peliculas':peliculas,
    }

    return render(request, 'pelicula_list.html', context)
