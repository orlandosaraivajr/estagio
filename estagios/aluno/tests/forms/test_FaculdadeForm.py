from django.test import TestCase

from estagios.aluno.forms import FaculdadeForm


class CadastroFormTest(TestCase):
    def test_form_has_fields(self):
        form = FaculdadeForm()
        expected = ['curso', 'instituicao', 'situacao']
        expected = expected + ['carga_horaria', 'data_inicio', 'data_fim']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_obrigatorio_instituicao(self):
        form = self.make_validated_form(instituicao='')
        self.assertFormErrorCode(form, 'instituicao', 'required')

    def test_obrigatorio_curso(self):
        form = self.make_validated_form(curso='')
        self.assertFormErrorCode(form, 'curso', 'required')

    def test_obrigatorio_data_inicio(self):
        form = self.make_validated_form(data_inicio='')
        self.assertFormErrorCode(form, 'data_inicio', 'required')

    def test_necessario_informar_instituicao(self):
        form = self.make_validated_form(instituicao='')
        self.assertListEqual(['instituicao'], list(form.errors))

    def test_necessario_curso(self):
        form = self.make_validated_form(curso='')
        self.assertListEqual(['curso'], list(form.errors))

    def test_necessario_data_inicio(self):
        form = self.make_validated_form(data_inicio='')
        self.assertListEqual(['data_inicio'], list(form.errors))

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
        valid = dict(data_inicio=datetime(2019, 1, 1, 0, 0, 0, 127325, tzinfo=pytz.UTC),
                     curso='nome_do_curso',
                     instituicao='fho',
                     situacao='0',
                     )
        data = dict(valid, **kwargs)
        form = FaculdadeForm(data)
        form.is_valid()
        return form
