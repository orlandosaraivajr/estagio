from django.shortcuts import resolve_url as r
from django.test import Client, TestCase

from estagios.aluno.forms import RedesSociaisForm
from estagios.aluno.models import RedesSociaisModel
from estagios.core.functions import registro_novo_aluno
from estagios.core.models import User

view_in_test = 'aluno:aluno_redes_sociais'
template_in_test = 'aluno_redes_sociais.html'


class AlunoGet(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            'admin',
            'eu@me.com',
            '123',
            is_student=True)
        cadastro = RedesSociaisModel()
        cadastro.user = User.objects.get(email='eu@me.com')
        cadastro.save()
        self.client.login(username='admin', password='123')
        self.resp = self.client.get(r(view_in_test))

    def test_template(self):
        self.assertTemplateUsed(self.resp, template_in_test)

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_html_template(self):
        tags = (
            ('Estágio Nota 10', 2),
            ('Contato', 1),
            ('Faculdade', 1),
            ('Outros cursos', 1),
            ('Empregos Anteriores', 1),
            ('Sair', 3),
            ('<form', 2),
            ('</form>', 2),
            ('<input', 5),
            ('type="submit"', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class AlunoPostOK(TestCase):
    def setUp(self):
        registro_novo_aluno('eu@me.com', '123')
        self.client = Client()
        self.client.login(username='eu@me.com', password='123')
        self.data = dict(
            github='http://www.google.com',
            linkedin='http://www.google.com',
            facebook='http://www.google.com',
            portfolio='http://www.google.com'
        )
        self.resp = self.client.post(r(view_in_test), self.data)
        self.user = User.objects.get(username='eu@me.com')

    def test_github(self):
        armazenado = RedesSociaisModel.objects.get(user=self.user)
        self.assertEqual(self.data['github'], armazenado.github)

    def test_linkedin(self):
        armazenado = RedesSociaisModel.objects.get(user=self.user)
        self.assertEqual(self.data['linkedin'], armazenado.linkedin)

    def test_facebook(self):
        armazenado = RedesSociaisModel.objects.get(user=self.user)
        self.assertEqual(self.data['facebook'], armazenado.facebook)

    def test_portfolio(self):
        armazenado = RedesSociaisModel.objects.get(user=self.user)
        self.assertEqual(self.data['portfolio'], armazenado.portfolio)

    def test_template(self):
        self.assertTemplateUsed(self.resp, template_in_test)

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, RedesSociaisForm)


class AlunoPostFail(TestCase):
    def setUp(self):
        registro_novo_aluno('eu@me.com', '123')
        self.client = Client()
        self.client.login(username='eu@me.com', password='123')
        self.data = dict(
            github='http://www.google.com',
            linkedin='http://www.google.com',
            facebook='http://www.google.com',
            portfolio='http://www.google.com'
        )
        self.resp = self.client.post(r(view_in_test), self.data)
        data_error = dict(
            github='error_url',
            linkedin='error_url',
            facebook='error_url',
            portfolio='error_url'
        )
        self.resp = self.client.post(r(view_in_test), data_error)
        self.user = User.objects.get(username='eu@me.com')

    def test_github(self):
        armazenado = RedesSociaisModel.objects.get(user=self.user)
        self.assertEqual(self.data['github'], armazenado.github)

    def test_linkedin(self):
        armazenado = RedesSociaisModel.objects.get(user=self.user)
        self.assertEqual(self.data['linkedin'], armazenado.linkedin)

    def test_facebook(self):
        armazenado = RedesSociaisModel.objects.get(user=self.user)
        self.assertEqual(self.data['facebook'], armazenado.facebook)

    def test_portfolio(self):
        armazenado = RedesSociaisModel.objects.get(user=self.user)
        self.assertEqual(self.data['portfolio'], armazenado.portfolio)

    def test_linkedin(self):
        armazenado = RedesSociaisModel.objects.get(user=self.user)
        self.assertEqual(self.data['linkedin'], armazenado.linkedin)

    def test_facebook(self):
        armazenado = RedesSociaisModel.objects.get(user=self.user)
        self.assertEqual(self.data['facebook'], armazenado.facebook)

    def test_portfolio(self):
        armazenado = RedesSociaisModel.objects.get(user=self.user)
        self.assertEqual(self.data['portfolio'], armazenado.portfolio)

    def test_template(self):
        self.assertTemplateUsed(self.resp, template_in_test)

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, RedesSociaisForm)
