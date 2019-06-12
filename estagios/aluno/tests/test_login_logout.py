from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url as r
from django.test import Client, TestCase


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
        self.client = Client()
        User.objects.create_user(
            'admin',
            'eu@me.com',
            '123',
            is_student=True)
        data = {'username': 'eu@me.com', 'password': '123'}
        self.resp = self.client.post(r('aluno:aluno_login'), data)

    def test_302_response(self):
        self.assertEqual(302, self.resp.status_code)


class LoginPostTestFollow(TestCase):
    def setUp(self):
        User = get_user_model()
        self.client = Client()
        User.objects.create_user(
            'admin',
            'eu@me.com',
            '123',
            is_student=True)
        data = {'username': 'eu@me.com', 'password': '123'}
        self.resp = self.client.post(r('aluno:aluno_login'), data, follow=True)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'aluno_index.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)


class LoginPostTestFail(TestCase):
    def setUp(self):
        User = get_user_model()
        self.client = Client()
        User.objects.create_user(
            'admin',
            'eu@me.com',
            '123')
        data = {'username': 'eu@me.com', 'password': 'senha_errada'}
        self.resp = self.client.post(r('aluno:aluno_login'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'aluno_login.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_labels_html(self):
        tags = (
            ('Login', 2),
            ('<input', 4),
            ('<input type="hidden"', 1),
            ('<input type="email"', 1),
            ('<input type="password"', 1),
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
