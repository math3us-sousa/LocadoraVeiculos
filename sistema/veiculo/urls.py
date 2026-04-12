from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('', listarVeiculos.as_view(), name='listar-veiculos'),
]
