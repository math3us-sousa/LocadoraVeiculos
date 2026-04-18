from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='E-mail',
        help_text='Obrigatório. Usado para recuperação de senha.',
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.email = self.cleaned_data['email']
        if commit:
            usuario.save()
        return usuario
