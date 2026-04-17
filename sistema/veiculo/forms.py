from django.forms import ModelForm
from veiculo.models import Veiculo

class FormularioVeiculo(ModelForm):

    '''Formulário para criar ou editar um veículo. Baseado no modelo Veiculo.'''

    class Meta:
        model = Veiculo
        exclude = []
