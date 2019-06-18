from django.test import TestCase

from estagios.aluno.forms import CadastroForm


class CadastroFormTest(TestCase):
    def test_form_has_fields(self):
        form = CadastroForm()
        expected = ['data_nascimento', 'sobre_voce']
        expected = expected + ['objetivos_profissionais', 'sexo', 'deficiencia']
        expected = expected + ['telefone', 'celular', 'telefone_recado']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_obrigatorio_objetivos_profissionais(self):
        form = self.make_validated_form(objetivos_profissionais='')
        self.assertFormErrorCode(form, 'objetivos_profissionais', 'required')

    def test_obrigatorio_sobre_voce(self):
        form = self.make_validated_form(sobre_voce='')
        self.assertFormErrorCode(form, 'sobre_voce', 'required')

    def test_obrigatorio_sobre_data_nascimento(self):
        form = self.make_validated_form(data_nascimento='')
        self.assertFormErrorCode(form, 'data_nascimento', 'required')

    def test_necessario_informar_objetivos_profissionais(self):
        form = self.make_validated_form(objetivos_profissionais='')
        self.assertListEqual(['objetivos_profissionais'], list(form.errors))

    def test_necessario_informar_sobre_voce(self):
        form = self.make_validated_form(sobre_voce='')
        self.assertListEqual(['sobre_voce'], list(form.errors))

    def test_necessario_informar_data_nascimento(self):
        form = self.make_validated_form(data_nascimento='')
        self.assertListEqual(['data_nascimento'], list(form.errors))

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
        from datetime import datetime
        import pytz
        valid = dict(data_nascimento=datetime(1981, 12, 30, 10, 20, 10, 127325, tzinfo=pytz.UTC),
                     sobre_voce='12345678901',
                     objetivos_profissionais='henrique@bastos.net',
                     sexo='1',
                     deficiencia='0',
                     telefone='19 9999-9999',
                     celular='19 9999-9999',
                     telefone_recado='19 9999-9999'
                     )
        data = dict(valid, **kwargs)
        form = CadastroForm(data)
        form.is_valid()
        return form
