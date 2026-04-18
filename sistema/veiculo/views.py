from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import Http404, FileResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from veiculo.models import Veiculo
from veiculo.consts import MARCA_CHOICES, COR_CHOICES, COMBUSTIVEL_CHOICES
from .forms import FormularioVeiculo


class listarVeiculos(LoginRequiredMixin, ListView):
    model = Veiculo
    template_name = 'veiculo/listar.html'
    context_object_name = 'veiculos'

    def get_queryset(self):
        queryset = super().get_queryset()
        busca = self.request.GET.get('busca', '').strip()

        if not busca:
            return queryset

        
        filtro = Q(modelo__icontains=busca) | Q(ano__icontains=busca)

        
        marcas = [cod for cod, nome in MARCA_CHOICES if busca.lower() in nome.lower()]
        if marcas:
            filtro |= Q(marca__in=marcas)

        
        cores = [cod for cod, nome in COR_CHOICES if busca.lower() in nome.lower()]
        if cores:
            filtro |= Q(cor__in=cores)

        combustiveis = [cod for cod, nome in COMBUSTIVEL_CHOICES if busca.lower() in nome.lower()]
        if combustiveis:
            filtro |= Q(combustivel__in=combustiveis)

        return queryset.filter(filtro)


class FotoVeiculo(LoginRequiredMixin, View):
    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto do veículo não encontrada.")


class CriarVeiculo(LoginRequiredMixin, CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')


class EditarVeiculo(LoginRequiredMixin, UpdateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')


class ExcluirVeiculo(LoginRequiredMixin, DeleteView):
    model = Veiculo
    template_name = 'veiculo/deletar.html'
    success_url = reverse_lazy('listar-veiculos')
