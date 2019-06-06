from django.shortcuts import resolve_url as r
from django.test import Client, TestCase

from estagios.core.models import User


class AlunoAuthGetHome(TestCase):
    def setUp(self):
        self.username = 'admin'
        self.password = '123mudar'
        self.client = Client()
        User.objects.create_user(
            self.username,
            'admin@admin.com',
            self.password,
            is_student=True)
        self.client.login(username=self.username,
                          password=self.password)

        self.resp = self.client.get(r('aluno:aluno_home'))

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'aluno_index.html')

    def test_200_template_home(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html_template_home(self):
        tags = (
            ('Start Bootstrap', 1),
            ('Dashboard', 2),
            ('Charts', 1),
            ('New Messages!', 1),
            ('New Tasks!', 1)
            )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class NotAlunoGetHome(TestCase):
    def setUp(self):
        self.username = 'admin'
        self.password = '123mudar'
        self.client = Client()
        User.objects.create_user(
            self.username,
            'admin@admin.com',
            self.password,
            is_student=False)
        self.client.login(username=self.username,
                          password=self.password)
        self.resp = self.client.get(r('aluno:aluno_home'))

    def test_302_template_home(self):
        self.assertEqual(302, self.resp.status_code)


class AnonymousGetHome(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('aluno:aluno_home'))

    def test_302_template_home(self):
        self.assertEqual(302, self.resp.status_code)


class AlunoGetCadastro(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('aluno:aluno_cadastro_dados_pessoais'))

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'aluno_cadastro.html')

    def test_200_template_home(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html_template_home(self):
        tags = (
            ('Start Bootstrap', 1),
            ('Dashboard', 2),
            ('Charts', 1),
            )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
