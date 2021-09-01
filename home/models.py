from django.db import models
from django.utils import timezone



class Empresa(models.Model):
    nome = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    logo = models.ImageField(blank=True, upload_to='logos/%y/%m/%d/')
    def __str__(self):
        return self.nome

class Empresa(models.Model):
    nome = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    logo = models.ImageField(blank=True, upload_to='logos/%y/%m/%d/')

    def __str__(self):
        return self.nome

class Game(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=700)
    Genero = models.CharField(max_length=200)
    Plataforma = models.CharField(max_length=150)
    dataLançamento = models.DateTimeField(default=timezone.now())
    mostrar = models.BooleanField(default=True)
    Desenvolvedora = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    foto = models.ImageField(blank=True, upload_to='fotos/%y/%m/%d/')


    def __str__(self):
        return self.nome