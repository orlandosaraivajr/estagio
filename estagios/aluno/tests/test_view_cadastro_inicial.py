from django.shortcuts import resolve_url as r
from django.test import Client, TestCase

from estagios.aluno.views import efetivar_cadastro_aluno
from estagios.core.functions import auth_request
from estagios.core.models import User

view_in_test = 'aluno:aluno_cadastro_inicial'
template_sem_login = 'aluno_cadastro_inicial.html'
template_com_login = 'aluno_index.html'


class NovoAlunoGet(TestCase):
    def setUp(self):
        self.client = Client()
        self.resp = self.client.get(r(view_in_test))

    def test_template(self):
        self.assertTemplateUsed(self.resp, template_sem_login)

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)


class NovoAlunoPost(TestCase):
    def setUp(self):
        self.client = Client()
        data = {
            'username': 'eu@me.com',
            'password': '123'
        }
        self.resp = self.client.post(r(view_in_test), data)

    def test_created_user(self):
        user = User.objects.get(email='eu@me.com')
        self.assertEqual(user.username, 'eu@me.com')

    def test_created_user_student(self):
        user = User.objects.get(email='eu@me.com')
        self.assertTrue(user.is_student)

    def test_created_user_is_not_teacher(self):
        user = User.objects.get(email='eu@me.com')
        self.assertFalse(user.is_teacher)

    def test_created_user_is_not_worker(self):
        user = User.objects.get(email='eu@me.com')
        self.assertFalse(user.is_worker)

    def test_302_template(self):
        self.assertEqual(302, self.resp.status_code)


class NovoAlunoPostFollow(TestCase):
    def setUp(self):
        self.client = Client()
        data = {
            'username': 'eu@me.com',
            'password': '123'
        }
        self.resp = self.client.post(
            r(view_in_test),
            data,
            follow=True
        )

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, template_com_login)
