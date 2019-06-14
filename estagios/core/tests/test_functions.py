from django.contrib.auth import get_user_model
from django.test import TestCase

from estagios.core.functions import authenticate, registro_novo_aluno
from estagios.core.models import User


class registro_novo_aluno_Test(TestCase):
    def setUp(self):
        User = get_user_model()
        registro_novo_aluno('user@me.com', 'segredo')

    def test_created(self):
        self.assertTrue(User.objects.exists())

    def test_username(self):
        user = User.objects.get(username='user@me.com')
        self.assertEqual(user.username, 'user@me.com')

    def test_estudante(self):
        username = User.objects.get(username='user@me.com')
        self.assertTrue(username.is_student)

    def test_professor(self):
        username = User.objects.get(username='user@me.com')
        self.assertFalse(username.is_teacher)

    def test_empresa(self):
        username = User.objects.get(username='user@me.com')
        self.assertFalse(username.is_worker)


class authenticate_Fail_Test(TestCase):
    def setUp(self):
        self.retorno = authenticate('user@me.com', 'segredo')

    def test_null(self):
        self.assertFalse(self.retorno)


class authenticate_OK_Test(TestCase):
    def setUp(self):
        registro_novo_aluno('user@me.com', 'segredo')
        self.retorno = authenticate('user@me.com', 'segredo')

    def test_auth_ok(self):
        user = User.objects.get(email='user@me.com')
        self.assertEqual(self.retorno, user)

    def test_auth_ok_2(self):
        user = User.objects.get(username='user@me.com')
        self.assertEqual(self.retorno, user)
