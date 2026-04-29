from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

from anuncios.models import Anuncio
from anuncios.forms import FormularioAnuncio


class ListarAnuncios(LoginRequiredMixin, ListView):
    model = Anuncio
    template_name = 'anuncios/listar.html'
    context_object_name = 'anuncios'
    ordering = ['-data_criacao']

    def get_queryset(self):
        queryset = super().get_queryset()
        busca = self.request.GET.get('busca', '').strip()
        if busca:
            queryset = queryset.filter(
                Q(titulo__icontains=busca) |
                Q(descricao__icontains=busca) |
                Q(veiculo__modelo__icontains=busca)
            )
        return queryset


class CriarAnuncio(LoginRequiredMixin, CreateView):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncios/novo.html'
    success_url = reverse_lazy('listar-anuncios')

    def form_valid(self, form):
        # Preenche o usuario automaticamente com quem está logado
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class EditarAnuncio(LoginRequiredMixin, UpdateView):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncios/editar.html'
    success_url = reverse_lazy('listar-anuncios')


class ExcluirAnuncio(LoginRequiredMixin, DeleteView):
    model = Anuncio
    template_name = 'anuncios/deletar.html'
    success_url = reverse_lazy('listar-anuncios')
