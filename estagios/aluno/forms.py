from django import forms
from django.forms import ModelForm

from estagios.aluno.models import CHOICES_DEFICIENCIA, CHOICES_SEXO, CadastroModel


class CadastroForm(ModelForm):
    error_css_class = "error"

    class Meta:
        model = CadastroModel
        fields = ('data_nascimento', 'sobre_voce')
        fields = fields + ('objetivos_profissionais', 'sexo', 'deficiencia')
        fields = fields + ('telefone', 'celular', 'telefone_recado')

        labels = {
            'data_nascimento': 'Data de Nascimento:',
            'sobre_voce': 'Fale sobre você',
            'objetivos_profissionais': 'Fale sobre seub objetivos profissionais',
            'sexo': 'Sexo: ',
            'deficiencia': 'Possui alguma limitação ? ',
            'telefone': 'Telefone Fixo:',
            'celular': 'Telefone celular:',
            'telefone_recado': 'Telefone para recado:',
        }
        widgets = {
            'data_nascimento': forms.DateInput(
                attrs={'class': 'form-control fa fa-calendar'}
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
                'cols': 15
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
