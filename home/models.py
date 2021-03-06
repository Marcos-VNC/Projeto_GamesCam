from django.db import models
from django.utils import timezone



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
    dataLanĂ§amento = models.DateTimeField(default=timezone.now())
    mostrar = models.BooleanField(default=True)
    Desenvolvedora = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    foto = models.ImageField(blank=True, upload_to='fotos/%y/%m/%d/')


    def __str__(self):
        return self.nome

class ImagesGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    img01 = models.ImageField(blank=True, upload_to='imagesGame/%y/%m/%d/')
    img02 = models.ImageField(blank=True, upload_to='imagesGame/%y/%m/%d/')
    img03 = models.ImageField(blank=True, upload_to='imagesGame/%y/%m/%d/')
