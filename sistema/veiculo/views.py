from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from veiculo.models import Veiculo
from django.views.generic import View
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse


class listarVeiculos(LoginRequiredMixin, ListView):

    '''View para listar os veículos disponíveis. Requer que o usuário esteja autenticado.'''

    model = Veiculo
    template_name = 'veiculo/listar.html'
    context_object_name = 'veiculos'

   
    
class FotoVeiculo(LoginRequiredMixin,View):

    '''View para servir as fotos dos veículos. Recebe o nome do arquivo como parâmetro.'''

    def get(self, request, arquivo):
        try:
           veiculo= Veiculo.objects.get(foto='veiculo/fotos/{}'.format)
           return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto do veículo não encontrada.")
        except Exception as exception:
            raise exception

#class CriarVeiculo(LoginRequiredMixin, View):
    
    #'''View para criar um novo veículo. Requer que o usuário esteja autenticado.'''

    #dmodel = Veiculo
    #form_class = FormularioVeiculo
    #template_name = 'veiculo/novo.html'
    #success_url = reverse_lazy('listar-veiculos')

#class EditarVeiculo(LoginRequiredMixin, View):
    
    #'''View para editar um veículo existente. Requer que o usuário esteja autenticado.'''

    #model = Veiculo
    #form_class = FormularioVeiculo
    #template_name = 'veiculo/editar.html'
    #success_url = reverse_lazy('listar-veiculos')
