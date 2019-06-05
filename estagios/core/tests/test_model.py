from django.contrib.auth import get_user_model
from django.test import TestCase

from estagios.core.models import User


class UserModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.cadastro = User(
            username='orlandosaraivajr',
            email='orlandosaraivajr@gmail.com',
            password='segredo',
            first_name='Orlando',
            last_name='Saraiva Jr',
            )
        self.cadastro.save()

    def test_created(self):
        self.assertTrue(User.objects.exists())

    def test_username(self):
        username = self.cadastro.username
        self.assertEqual(username, 'orlandosaraivajr')

    def test_email(self):
        email = self.cadastro.email
        self.assertEqual(email, 'orlandosaraivajr@gmail.com')

    def test_password(self):
        password = self.cadastro.password
        self.assertEqual(password, 'segredo')

    def test_first_name(self):
        first_name = self.cadastro.first_name
        self.assertEqual(first_name, 'Orlando')

    def test_last_name(self):
        last_name = self.cadastro.last_name
        self.assertEqual(last_name, 'Saraiva Jr')

    def test_estudante(self):
        self.assertFalse(self.cadastro.is_student)

    def test_professor(self):
        self.assertFalse(self.cadastro.is_teacher)

    def test_empresa(self):
        self.assertFalse(self.cadastro.is_worker)
