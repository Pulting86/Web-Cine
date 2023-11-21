from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Asiento(models.Model):
    reservado = models.BooleanField()
    cliente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class Sala(models.Model):
    numero = models.CharField(max_length=200)
    asiento=models.ManyToManyField(Asiento)


    class Meta:
        ordering = ['numero']

    def str(self) -> str:
        return str(self.numero)

    def get_absolute_url(self):
        return reverse('pelicula_list', args=[str(self.id)])


class Sesion(models.Model):
    horario = models.TimeField()

    class Meta:
        ordering = ['horario']

    def __str__(self) -> str:
        return str(self.horario)
    
    def get_absolute_url(self):
        return reverse('pelicula_list', args=[str(self.id)])


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    sala = models.ManyToManyField(Sala)
    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['titulo', 'sesion']

    def __str__(self) -> str:
        return self.titulo

    def get_absolute_url(self):
        return reverse('pelicula_details', args=[str(self.id)])
    
class Copia(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    sala = models.ManyToManyField(Sala)
    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.pelicula)
    
    def get_absolute_url(self):
        return reverse('pelicula_details', args=[str(self.pelicula.id)])
    

class API_Pelicula(models.Model):
    pelicula_id = models.ForeignKey(Pelicula, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.TextField()
    photo = models.URLField()




class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)

    def __str__(self): 
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()
    
