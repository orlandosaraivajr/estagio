from django.test import TestCase

from estagios.core.form import LoginForm


class LoginFormTest(TestCase):
    def setUp(self):
        self.form = LoginForm()

    def test_form_has_fields(self):
        expected = ['email', 'password']
        self.assertSequenceEqual(expected, list(self.form.fields))


class CleanFormTest(TestCase):
    def setUp(self):
        data = {}
        data['email'] = 'eu@me.com'
        data['password'] = '123'
        self.form = LoginForm(data)
        self.form.is_valid()

    def test_valid_form(self):
        self.assertTrue(self.form.is_valid())

    def test_email(self):
        self.assertEqual(self.form.cleaned_data['email'], 'eu@me.com')

    def test_password(self):
        self.assertEqual(self.form.cleaned_data['password'], '123')


class CleanFormFailTest(TestCase):
    def setUp(self):
        data = {}
        data['email'] = 'eu@me.com'
        self.form = LoginForm(data)
        self.form.is_valid()

    def test_valid_form(self):
        self.assertFalse(self.form.is_valid())

    def test_email(self):
        self.assertEqual(self.form.cleaned_data['email'], 'eu@me.com')

    def test_password(self):
        try:
            self.form.cleaned_data['password']
        except KeyError:
            self.assertTrue(True)
