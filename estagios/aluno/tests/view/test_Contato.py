from django.shortcuts import resolve_url as r
from django.test import Client, TestCase

from estagios.aluno.forms import ContatoForm
from estagios.aluno.models import ContatoModel
from estagios.core.functions import registro_novo_aluno
from estagios.core.models import User

view_in_test = 'aluno:aluno_contato'
template_in_test = 'aluno_contato.html'


class AlunoGet(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            'admin',
            'eu@me.com',
            '123',
            is_student=True)
        cadastro = ContatoModel()
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
            ('Contato', 3),
            ('Faculdade', 1),
            ('Outros cursos', 1),
            ('Empregos Anteriores', 1),
            ('Sair', 3)
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
            endereco='Rua Teste',
            endereco_numero='15',
            endereco_cidade='São Paulo',
            endereco_estado='SP'
        )
        self.resp = self.client.post(r(view_in_test), self.data)
        self.user = User.objects.get(username='eu@me.com')

    def test_endereco(self):
        armazenado = ContatoModel.objects.get(user=self.user)
        self.assertEqual(self.data['endereco'], armazenado.endereco)

    def test_endereco_numero(self):
        armazenado = ContatoModel.objects.get(user=self.user)
        self.assertEqual(self.data['endereco_numero'], armazenado.endereco_numero)

    def test_endereco_cidade(self):
        armazenado = ContatoModel.objects.get(user=self.user)
        self.assertEqual(self.data['endereco_cidade'], armazenado.endereco_cidade)

    def test_endereco_estado(self):
        armazenado = ContatoModel.objects.get(user=self.user)
        self.assertEqual(self.data['endereco_estado'], armazenado.endereco_estado)

    def test_template(self):
        self.assertTemplateUsed(self.resp, template_in_test)

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, ContatoForm)


class AlunoPostFail(TestCase):
    def setUp(self):
        registro_novo_aluno('eu@me.com', '123')
        self.client = Client()
        self.client.login(username='eu@me.com', password='123')
        self.data = dict(
            endereco='Rua Teste',
            endereco_numero='15',
            endereco_cidade='São Paulo',
            endereco_estado='SP'
        )
        self.resp = self.client.post(r(view_in_test), self.data)
        self.data_error = dict(
        )
        self.resp = self.client.post(r(view_in_test), self.data_error)
        self.user = User.objects.get(username='eu@me.com')

    def test_nao_atualizar_endereco(self):
        armazenado = ContatoModel.objects.get(user=self.user)
        self.assertEqual(self.data['endereco'], armazenado.endereco)

    def test_nao_atualizar_endereco_numero(self):
        armazenado = ContatoModel.objects.get(user=self.user)
        self.assertEqual(self.data['endereco_numero'], armazenado.endereco_numero)

    def test_nao_atualizar_endereco_cidade(self):
        armazenado = ContatoModel.objects.get(user=self.user)
        self.assertEqual(self.data['endereco_cidade'], armazenado.endereco_cidade)

    def test_nao_atualizar_endereco_estado(self):
        armazenado = ContatoModel.objects.get(user=self.user)
        self.assertEqual(self.data['endereco_estado'], armazenado.endereco_estado)

    def test_template(self):
        self.assertTemplateUsed(self.resp, template_in_test)

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, ContatoForm)
