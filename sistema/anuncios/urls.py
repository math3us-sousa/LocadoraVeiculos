from django.urls import path
from anuncios.views import ListarAnuncios, CriarAnuncio, EditarAnuncio, ExcluirAnuncio

urlpatterns = [
    path('', ListarAnuncios.as_view(), name='listar-anuncios'),
    path('novo/', CriarAnuncio.as_view(), name='criar-anuncio'),
    path('editar/<int:pk>/', EditarAnuncio.as_view(), name='editar-anuncio'),
    path('excluir/<int:pk>/', ExcluirAnuncio.as_view(), name='excluir-anuncio'),
]
