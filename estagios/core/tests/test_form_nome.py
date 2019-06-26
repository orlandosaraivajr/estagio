from django.test import TestCase

from estagios.core.form import NomeCompletoForm


class NomeUsuarioFormTest(TestCase):
    def setUp(self):
        self.form = NomeCompletoForm()

    def test_form_has_fields(self):
        expected = ['first_name']
        self.assertSequenceEqual(expected, list(self.form.fields))


class Form_name_Test(TestCase):
    def setUp(self):
        data = {}
        data['first_name'] = 'User'
        self.form = NomeCompletoForm(data)
        self.form.is_valid()

    def test_valid_form(self):
        self.assertTrue(self.form.is_valid())

    def test_email(self):
        self.assertEqual(self.form.cleaned_data['first_name'], 'User')


class Form_no_name_Test(TestCase):
    def setUp(self):
        data = {}
        data['first_name'] = ''
        self.form = NomeCompletoForm(data)
        self.form.is_valid()

    def test_username(self):
        self.assertEqual(
            self.form.cleaned_data['first_name'],
            'Nome em Branco')

    def test_valid_form(self):
        self.assertTrue(self.form.is_valid())
