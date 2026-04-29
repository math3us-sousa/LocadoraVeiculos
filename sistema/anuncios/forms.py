from django.forms import ModelForm
from anuncios.models import Anuncio


class FormularioAnuncio(ModelForm):
    '''Formulário para criar ou editar um anúncio. O campo usuario é preenchido
    automaticamente pela view com o usuário logado.'''

    class Meta:
        model = Anuncio
        exclude = ['usuario', 'data_criacao']
