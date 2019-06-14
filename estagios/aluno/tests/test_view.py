from django.shortcuts import resolve_url as r
from django.test import Client, TestCase

from estagios.core.models import User

view_template_list = [
    ('aluno:aluno_home', 'aluno_index.html'),
    ('aluno:aluno_sobre_mim', 'aluno_sobre_mim.html'),
    ('aluno:aluno_contato', 'aluno_contato.html'),
    ('aluno:aluno_faculdade', 'aluno_faculdade.html'),
    ('aluno:aluno_outros_cursos', 'aluno_outros_cursos.html'),
    ('aluno:aluno_outros_empregos', 'aluno_outros_empregos.html'),
    ('aluno:aluno_diario_aprendizado', 'aluno_diario_aprendizado.html'),
    ('aluno:aluno_esqueceu_senha', 'aluno_contato.html')

]


class GetRedirectTest(TestCase):
    def setUp(self):
        self.resp_list = []
        for view_test in view_template_list:
            self.resp_list.append(
                self.client.get(r(view_test[0]))
            )

    def test_302_response(self):
        for response in self.resp_list:
            with self.subTest():
                self.assertEqual(302, response.status_code)


class GetRedirectTestFollow(TestCase):
    def setUp(self):
        self.resp_list = []
        for view_test in view_template_list:
            self.resp_list.append(
                self.client.get(r(view_test[0]), follow=True)
            )

    def test_200_response(self):
        for response in self.resp_list:
            with self.subTest():
                self.assertEqual(200, response.status_code)

    def test_redirect_url(self):
        for response in self.resp_list:
            with self.subTest():
                self.assertEqual(
                    '/alunos/login/',
                    response.redirect_chain[0][0]
                )

    def test_template_used(self):
        for response in self.resp_list:
            with self.subTest():
                self.assertTemplateUsed(
                    response,
                    'aluno_login.html'
                )


class AlunoGet(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            'admin',
            'eu@me.com',
            '123',
            is_student=True)
        self.client.login(username='admin', password='123')
        self.resp_list = []
        for view_test in view_template_list:
            self.resp_list.append((
                self.client.get(r(view_test[0])),
                view_test[1]
            ))

    def test_template(self):
        for response in self.resp_list:
            with self.subTest():
                self.assertTemplateUsed(
                    response[0],
                    response[1]
                )

    def test_200_template(self):
        for response in self.resp_list:
            with self.subTest():
                self.assertEqual(
                    200,
                    response[0].status_code
                )


class NotAlunoGet(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            'admin',
            'eu@me.com',
            '123',
            is_student=False)
        self.client.login(username='admin', password='123')
        self.resp_list = []
        for view_test in view_template_list:
            self.resp_list.append(
                self.client.get(r(view_test[0]), follow=True)
            )

    def test_302_template(self):
        for response in self.resp_list:
            with self.subTest():
                self.assertTrue(
                    302,
                    response.status_code
                )


class NotAlunoGetFollow(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            'admin',
            'eu@me.com',
            '123',
            is_student=False)
        self.client.login(username='admin', password='123')
        self.resp_list = []
        for view_test in view_template_list:
            self.resp_list.append(
                self.client.get(r(view_test[0]), follow=True)
            )

    def test_200_template(self):
        for response in self.resp_list:
            with self.subTest():
                self.assertTrue(
                    200,
                    response.status_code
                )

    def test_redirect_url(self):
        for response in self.resp_list:
            with self.subTest():
                self.assertTrue(
                    '/',
                    response.redirect_chain[0][0]
                )

    def test_template_used(self):
        for response in self.resp_list:
            with self.subTest():
                self.assertTemplateUsed(
                    response,
                    'index.html'
                )


class AnonymousGet(TestCase):
    def setUp(self):
        self.resp_list = []
        for view_test in view_template_list:
            self.resp_list.append(
                self.client.get(r(view_test[0]), follow=True)
            )

    def test_302_template(self):
        for response in self.resp_list:
            with self.subTest():
                self.assertTrue(
                    302,
                    response.status_code
                )
