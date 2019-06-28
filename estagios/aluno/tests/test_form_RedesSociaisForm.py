from django.test import TestCase
from estagios.aluno.forms import RedesSociaisForm


class RedesSociaisFormTest(TestCase):
    def test_form_has_fields(self):
        form = RedesSociaisForm()
        expected = ['github', 'facebook']
        expected = expected + ['linkedin', 'portfolio']
        self.assertSequenceEqual(expected, list(form.fields))