from django import forms
from django.forms import ModelForm

from estagios.aluno.models import CadastroModel


class CadastroForm(ModelForm):
    class Meta:
        model = CadastroModel
        fields = ('user', 'data_nascimento', 'sobre_voce')
        fields = fields + ('objetivos_profissionais', 'sexo', 'deficiencia')
        fields = fields + ('telefone', 'celular', 'telefone_recado')

        labels = {
            'user': 'Usuário',
            'data_nascimento': 'Data de Nascimento',
            'sobre_voce': 'Fale sobre você',
            'objetivos_profissionais': 'Fale sobre seub objetivos profissionais',
            'sexo': 'Sexo',
            'deficiencia': 'Deficiencia',
            'telefone': 'Telefone Fixo',
            'celular': 'Telefone celular',
            'telefone_recado': 'Telefone para recado',
        }
        widgets = {
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'sobre_voce': forms.Textarea(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'empresa': {
                'required': ("Selecione a empresa fiscalizada."),
            },
            'imagem': {
                'required': ("Selecione uma foto da vistoria."),
            }
        }
