from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.shortcuts import resolve_url as r

class HomeGetRedirectTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('aluno:aluno_home'))

    def test_302_response(self):
        self.assertEqual(302, self.resp.status_code)


class LoginTemplateGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('aluno:aluno_login'))

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'aluno_login.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_labels_html(self):
        tags = (
            ('<form', 1),
            ('</form>', 1),
            ('<input', 4),
            ('<label>', 1),
            ('</label>', 3),
            ('submit', 1),
            ('button', 2),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class LoginPostTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.username = 'admin'
        self.password = '123mudar'
        self.client = Client()
        User.objects.create_user(
            self.username,
            'admin@admin.com',
            self.password)
        data = {}
        data['username'] = self.username
        data['password'] = self.password
        self.resp = self.client.post(r('aluno:aluno_login'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'aluno_index.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)


class LoginPostTestFail(TestCase):
    def setUp(self):
        User = get_user_model()
        self.username = 'admin'
        self.password = '123mudar'
        self.client = Client()
        User.objects.create_user(
            self.username,
            'admin@admin.com',
            self.password)
        data = {}
        data['username'] = 'usuario_errado'
        data['password'] = 'senha_errada'
        self.resp = self.client.post(r('aluno:aluno_login'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'aluno_login.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_labels_html(self):
        tags = (
            ('<form', 1),
            ('</form>', 1),
            ('<input', 4),
            ('<label>', 1),
            ('</label>', 3),
            ('submit', 1),
            ('button', 2)
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
