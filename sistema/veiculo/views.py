from django.shortcuts import render
from django.views.generic import ListView
from veiculo.models import Veiculo

class listarVeiculos(ListView):
    model = Veiculo
    template_name = 'veiculo/listar.html'
    context_object_name = 'veiculos'
