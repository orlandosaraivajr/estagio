from django.test import TestCase

from estagios.aluno.forms import CadastroForm


class CadastroFormTest(TestCase):
    def setUp(self):
        self.form = CadastroForm()

    def test_form_has_fields(self):
        expected = ['data_nascimento', 'sobre_voce']
        expected = expected + ['objetivos_profissionais', 'sexo', 'deficiencia']
        expected = expected + ['telefone', 'celular', 'telefone_recado']
        self.assertSequenceEqual(expected, list(self.form.fields))


class CleanFormTest(TestCase):
    pass


class CleanFormFailTest(TestCase):
    pass
