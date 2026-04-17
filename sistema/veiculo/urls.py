from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('', listarVeiculos.as_view(), name='listar-veiculos'),
    path('novo/', CriarVeiculo.as_view(), name='criar-veiculo'),
    path('editar/<int:pk>/', EditarVeiculo.as_view(), name='editar-veiculo'),
    path('excluir/<int:pk>/', ExcluirVeiculo.as_view(), name='excluir-veiculo'),

    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto-veiculo'),
]
