from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from veiculo.models import Veiculo


class listarVeiculos(LoginRequiredMixin, ListView):
    model = Veiculo
    template_name = 'veiculo/listar.html'
    context_object_name = 'veiculos'
