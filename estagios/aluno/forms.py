from django import forms
from django.forms import ModelForm

from estagios.aluno.models import CHOICES_DEFICIENCIA, CHOICES_SEXO, CadastroModel, ContatoModel, \
    CHOICES_ESTADOS_BRASILEIROS


class SobreMimForm(ModelForm):
    error_css_class = "error"

    class Meta:
        model = CadastroModel
        fields = ('data_nascimento', 'sobre_voce')
        fields = fields + ('objetivos_profissionais', 'sexo', 'deficiencia')
        fields = fields + ('telefone', 'celular', 'telefone_recado')

        labels = {
            'data_nascimento': 'Data de Nascimento:',
            'sobre_voce': 'Fale sobre você',
            'objetivos_profissionais': 'Fale sobre seus objetivos profissionais',
            'sexo': 'Sexo: ',
            'deficiencia': 'Possui alguma limitação ? ',
            'telefone': 'Telefone Fixo:',
            'celular': 'Telefone celular:',
            'telefone_recado': 'Telefone para recado:',
        }
        widgets = {
            'data_nascimento': forms.DateInput(
                attrs={
                    'class': 'form-control fa fa-calendar',
                    'placeholder': 'dd/mm/aaaa'
                }
            ),
            'sexo': forms.Select(choices=CHOICES_SEXO,
                                 attrs={
                                     'class': 'form-control'
                                 }),
            'deficiencia': forms.Select(choices=CHOICES_DEFICIENCIA,
                                        attrs={
                                            'class': 'form-control'
                                        }),

            'sobre_voce': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'cols': 15,
                'placeholder': 'Fale um pouco sobre você.'
            }),
            'objetivos_profissionais': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'cols': 15
            }),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone_recado': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'data_nascimento': {
                'required': ("Digite uma data Válida."),
            },
            'sobre_voce': {
                'required': ("Não deixe este campo em branco. Fale um pouco sobre você."),
            },
            'objetivos_profissionais': {
                'required': ("Não deixe este campo em branco. Fale sobre seus objetivos profissionais."),
            }
        }

    def clean_data_nascimento(self):
        return self.cleaned_data['data_nascimento']


class ContatoForm(ModelForm):
    error_css_class = "error"
    github = forms.URLField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Preencha com o link do seu GitHub (não obrigatório)',
                'class': 'form-control'
                   }
        ),
        required=False,
    )

    facebook = forms.URLField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Preencha com o link do seu Facebook (não obrigatório)',
                'class': 'form-control'
            }
        ),
        required=False,
    )

    linkedin = forms.URLField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Preencha com o link do seu Linkedin (não obrigatório)',
                'class': 'form-control'
            }
        ),
        required=False,
    )

    portfolio = forms.URLField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Preencha com o link do seu portfolio (não obrigatório)',
                'class': 'form-control'
            }
        ),
        required=False,
    )

    class Meta:
        model = ContatoModel
        fields = ('endereco', 'endereco_numero', 'endereco_complemento')
        fields = fields + ('endereco_cidade', 'endereco_estado')

        labels = {
            'endereco': 'Endereço: ',
            'endereco_numero': 'Número: ',
            'endereco_complemento': 'Complemento:',
            'endereco_cidade': 'Cidade:',
            'endereco_estado': 'Estado:',
        }
        widgets = {
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu endereço',
            }),
            'endereco_numero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número',
            }),
            'endereco_complemento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'apto, bloco, lote',
            }),
            'endereco_cidade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cidade',
            }),
            'endereco_estado': forms.Select(choices=CHOICES_ESTADOS_BRASILEIROS,
                                            attrs={
                                                'class': 'form-control'
                                            }),

        }
        error_messages = {
            'endereco': {
                'required': ('Digite um endereço.'),
            },
            'endereco_numero': {
                'required': ('Número'),
            },
            'endereco_cidade': {
                'required': ('Digite sua cidade.'),
            },
        }

    def clean_endereco(self):
        return self.cleaned_data['endereco']
