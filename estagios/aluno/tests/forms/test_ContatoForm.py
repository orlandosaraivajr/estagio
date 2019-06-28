from django.test import TestCase

from estagios.aluno.forms import ContatoForm


class ContatoFormTest(TestCase):
    def test_form_has_fields(self):
        form = ContatoForm()
        expected = ['endereco', 'endereco_numero', 'endereco_complemento']
        expected = expected + ['endereco_cidade', 'endereco_estado']
        expected = expected + ['telefone', 'celular', 'telefone_recado']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_obrigatorio_endereco(self):
        form = self.make_validated_form(endereco='')
        self.assertFormErrorCode(form, 'endereco', 'required')

    def test_obrigatorio_endereco_numero(self):
        form = self.make_validated_form(endereco_numero='')
        self.assertFormErrorCode(form, 'endereco_numero', 'required')

    def test_obrigatorio_endereco_cidade(self):
        form = self.make_validated_form(endereco_cidade='')
        self.assertFormErrorCode(form, 'endereco_cidade', 'required')

    def test_obrigatorio_endereco_estado(self):
        form = self.make_validated_form(endereco_estado='')
        self.assertFormErrorCode(form, 'endereco_estado', 'required')

    def test_necessario_endereco(self):
        form = self.make_validated_form(endereco='')
        self.assertListEqual(['endereco'], list(form.errors))

    def test_validar_endereco_numero(self):
        form = self.make_validated_form(endereco_numero='')
        self.assertListEqual(['endereco_numero'], list(form.errors))

    def test_validar_endereco_cidade(self):
        form = self.make_validated_form(endereco_cidade='')
        self.assertListEqual(['endereco_cidade'], list(form.errors))

    def test_validar_endereco_estado(self):
        form = self.make_validated_form(endereco_estado='')
        self.assertListEqual(['endereco_estado'], list(form.errors))

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(
            endereco='Rua Teste',
            endereco_numero='15',
            endereco_cidade='São Paulo',
            endereco_estado='SP'
        )
        data = dict(valid, **kwargs)
        form = ContatoForm(data)
        form.is_valid()
        return form
