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
