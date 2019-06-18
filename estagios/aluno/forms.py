from django import forms
from django.forms import ModelForm

from estagios.aluno.models import CHOICES_DEFICIENCIA, CHOICES_SEXO, CadastroModel


class CadastroForm(ModelForm):
    class Meta:
        model = CadastroModel
        fields = ('data_nascimento', 'sobre_voce')
        fields = fields + ('objetivos_profissionais', 'sexo', 'deficiencia')
        fields = fields + ('telefone', 'celular', 'telefone_recado')

        labels = {
            'data_nascimento': 'Data de Nascimento',
            'sobre_voce': 'Fale sobre você',
            'objetivos_profissionais': 'Fale sobre seub objetivos profissionais',
            'sexo': 'Sexo: ',
            'deficiencia': 'Possui alguma limitação ? ',
            'telefone': 'Telefone Fixo',
            'celular': 'Telefone celular',
            'telefone_recado': 'Telefone para recado',
            }
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'sexo': forms.Select(choices=CHOICES_SEXO,
                                 attrs={
                                     'class': 'form-control',
                                     'onChange': 'change_click_categoria_distrito()',
                                     }),
            'deficiencia': forms.Select(choices=CHOICES_DEFICIENCIA,
                                        attrs={
                                            'class': 'form-control',
                                            'onChange': 'change_click_categoria_distrito()',
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
                'required': ("Fale sobre você."),
                }
            }

    def clean_data_nascimento(self):
        pass
