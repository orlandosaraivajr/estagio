from django.shortcuts import resolve_url as r
from django.test import Client, TestCase

from estagios.core.models import User


def tested_view():
    return 'aluno:aluno_home'


def tested_template():
    return 'aluno_index.html'


class GetRedirectTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r(tested_view()))

    def test_302_response(self):
        self.assertEqual(302, self.resp.status_code)


class GetRedirectTestFollow(TestCase):
    def setUp(self):
        self.resp = self.client.get(r(tested_view()), follow=True)

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_redirect_url(self):
        self.assertEqual('/alunos/login/', self.resp.redirect_chain[0][0])

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'aluno_login.html')


class AlunoGet(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            'admin',
            'admin@admin.com',
            '123',
            is_student=True)
        self.client.login(username='admin', password='123')
        self.resp = self.client.get(r(tested_view()))

    def test_template(self):
        self.assertTemplateUsed(self.resp, tested_template())

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html_template(self):
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


class NotAlunoGet(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            'admin',
            'admin@admin.com',
            '123',
            is_student=False)
        self.client.login(username='admin', password='123')
        self.resp = self.client.get(r(tested_view()))

    def test_302_template(self):
        self.assertEqual(302, self.resp.status_code)


class NotAlunoGetFollow(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            'admin',
            'admin@admin.com',
            '123',
            is_student=False)
        self.client.login(username='admin', password='123')
        self.resp = self.client.get(r(tested_view()), follow=True)

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_redirect_url(self):
        self.assertEqual('/', self.resp.redirect_chain[0][0])

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')


class AnonymousGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r(tested_view()))

    def test_302_template(self):
        self.assertEqual(302, self.resp.status_code)
