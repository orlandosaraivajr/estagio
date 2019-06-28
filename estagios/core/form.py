from django import forms
from django.forms import ModelForm

from estagios.core.models import User


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

        labels = {
            'email': 'E-mail',
            'password': 'Senha'
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }
        help_texts = {
            'email': ('E-mail cadastrado.'),
            'password': ('Senha para acesso.'),
        }
        error_messages = {
            'email': {
                'required': ("Digite um e-mail válido."),
            },
            'password': {
                'required': ("Senha não pode ser em branco."),
            }
        }


class NomeCompletoForm(ModelForm):
    error_css_class = "error"

    class Meta:
        model = User
        fields = ('first_name',)

        labels = {
            'first_name': 'Nome Completo',

        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Preencha seu nome completo.'
                }
            ),
        }
        error_messages = {
            'first_name': {
                'required': ("Não deixe este campo em branco. Informe seu nome completo."),
            },
        }

    def clean_first_name(self):
        if self.cleaned_data['first_name'] != '':
            return self.cleaned_data['first_name']
        return 'Nome em Branco'
