from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url as r
from django.test import TestCase, RequestFactory

from estagios.core.functions import authenticate
from estagios.core.functions import registro_novo_aluno
from estagios.core.functions import auth_request
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


class auth_request_Test(TestCase):
    def setUp(self):
        self.request = RequestFactory()
        self.view = 'aluno:aluno_login'

    def test_data_ok_no_user_POST(self):
        data = {
            'username': 'eu@me.com',
            'password': '123'
        }
        request = self.request.post(r(self.view), data)
        self.assertFalse(auth_request(request))

    def test_data_ok_user_ok_POST(self):
        User = get_user_model()
        User.objects.create_user(
            'eu@me.com', 'eu@me.com', '123')
        data = {
            'username': 'eu@me.com',
            'password': '123'
        }
        request = self.request.post(r(self.view), data)
        from django.contrib.sessions.middleware import SessionMiddleware
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        self.assertTrue(auth_request(request))

    def test_no_data_POST(self):
        request = self.request.post(r(self.view))
        self.assertFalse(auth_request(request))
