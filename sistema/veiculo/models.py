from django.db import models
from veiculo.consts import *

class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=MARCA_CHOICES)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=COR_CHOICES)
    combustivel = models.SmallIntegerField(choices=COMBUSTIVEL_CHOICES)
    foto = models.ImageField(upload_to='veiculo/fotos', null=True, blank=True)
