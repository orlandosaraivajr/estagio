from django import forms
from django.forms import ModelForm

from estagios.aluno.models import (
    CHOICES_DEFICIENCIA, CHOICES_SEXO, SobreMimModel, ContatoModel,
    CHOICES_ESTADOS_BRASILEIROS, RedesSociaisModel,
    FaculdadeModel, CHOICES_SITUACAO_ACADEMICA)


class SobreMimForm(ModelForm):
    error_css_class = "error"

    class Meta:
        model = SobreMimModel
        fields = ('data_nascimento', 'sobre_voce')
        fields = fields + ('objetivos_profissionais', 'sexo', 'deficiencia')

        labels = {
            'data_nascimento': 'Data de Nascimento:',
            'sobre_voce': 'Fale sobre você',
            'objetivos_profissionais': 'Fale sobre seus objetivos profissionais',
            'sexo': 'Sexo: ',
            'deficiencia': 'Possui alguma limitação ? ',
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


class ContatoForm(ModelForm):
    error_css_class = "error"

    class Meta:
        model = ContatoModel
        fields = ('endereco', 'endereco_numero', 'endereco_complemento')
        fields = fields + ('endereco_cidade', 'endereco_estado')
        fields = fields + ('telefone', 'celular', 'telefone_recado')

        labels = {
            'endereco': 'Endereço: ',
            'endereco_numero': 'Número: ',
            'endereco_complemento': 'Complemento:',
            'endereco_cidade': 'Cidade:',
            'endereco_estado': 'Estado:',
            'telefone': 'Telefone:',
            'celular': 'Celular:',
            'telefone_recado': 'Telefone Recado:',
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
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefone',
            }),
            'celular': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Celular',
            }),
            'telefone_recado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefone para Contato',
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


class RedesSociaisForm(ModelForm):
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
        model = RedesSociaisModel
        fields = ()


class FaculdadeForm(ModelForm):
    error_css_class = "error"

    class Meta:
        model = FaculdadeModel
        fields = ('curso', 'instituicao','situacao')
        fields = fields + ('carga_horaria', 'data_inicio', 'data_fim')

        labels = {
            'curso': 'Nome do curso',
            'instituicao': 'Instituição: ',
            'situacao': 'Situação ',
            'data_inicio': 'Data de início:',
            'data_fim': 'Data encerramento / previsão:',
            'carga_horaria': 'Carga Horária do curso:',
        }
        widgets = {
            'curso': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Curso',
            }),
            'instituicao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Faculdade / Universidade',
            }),
            'situacao': forms.Select(choices=CHOICES_SITUACAO_ACADEMICA,attrs={
                                         'class': 'form-control'
                                     }),
            'data_inicio': forms.DateInput(attrs={
                    'class': 'form-control fa fa-calendar',
                    'placeholder': 'dd/mm/aaaa'
                }),
            'data_fim': forms.DateInput(attrs={
                    'class': 'form-control fa fa-calendar',
                    'placeholder': 'dd/mm/aaaa'
                }),
            'carga_horaria': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Carga horária do curso',
            }),
        }
        error_messages = {
            'data_inicio': {
                'required': ("Digite uma data de início."),
            },
            'curso': {
                'required': ("Digite o nome do curso"),
            },
            'instituicao': {
                'required': ("Digite o nome da faculdade / universidade"),
            }
        }
