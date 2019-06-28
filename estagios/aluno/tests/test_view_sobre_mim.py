from datetime import datetime

import pytz
from django.shortcuts import resolve_url as r
from django.test import Client, TestCase

from estagios.aluno.forms import SobreMimForm
from estagios.aluno.models import SobreMimModel
from estagios.core.functions import registro_novo_aluno
from estagios.core.models import User

view_in_test = 'aluno:aluno_sobre_mim'
template_in_test = 'aluno_sobre_mim.html'


class AlunoGet(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            'eu@me.com',
            'eu@me.com',
            '123',
            is_student=True)
        cadastro = SobreMimModel()
        cadastro.user = User.objects.get(email='eu@me.com')
        cadastro.data_nascimento = datetime(2000, 1, 1, 0, 0, 0, tzinfo=pytz.UTC)
        cadastro.save()
        self.client.login(username='eu@me.com', password='123')
        self.resp = self.client.get(r(view_in_test))

    def test_template(self):
        self.assertTemplateUsed(self.resp, template_in_test)

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SobreMimForm)


class AlunoPostOK(TestCase):
    def setUp(self):
        registro_novo_aluno('eu@me.com', '123')
        self.client = Client()
        self.client.login(username='eu@me.com', password='123')
        data = dict(first_name='José da Silva',
                    data_nascimento='30/12/1981',
                    sobre_voce='Sou nota 10',
                    objetivos_profissionais='quero ser rico',
                    sexo='1',
                    deficiencia='0',
                    telefone='19 9999-9999',
                    celular='19 9999-9999',
                    telefone_recado='19 9999-9999'
                    )
        self.resp = self.client.post(r(view_in_test), data)

    def test_atualizado_nome_completo(self):
        user = User.objects.get(username='eu@me.com')
        nome_completo = user.first_name
        self.assertEqual('José da Silva', nome_completo)

    def test_atualizado_sobre_voce(self):
        user = User.objects.get(username='eu@me.com')
        armazenado = SobreMimModel.objects.get(user=user)
        self.assertEqual('Sou nota 10', armazenado.sobre_voce)

    def test_atualizado_objetivos_profissionais(self):
        user = User.objects.get(username='eu@me.com')
        armazenado = SobreMimModel.objects.get(user=user)
        self.assertEqual('quero ser rico', armazenado.objetivos_profissionais)

    def test_template(self):
        self.assertTemplateUsed(self.resp, template_in_test)

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SobreMimForm)


class AlunoPostFail(TestCase):
    def setUp(self):
        registro_novo_aluno('eu@me.com', '123')
        self.client = Client()
        self.client.login(username='eu@me.com', password='123')
        data = dict(data_nascimento='30/12/1981',
                    sobre_voce='',
                    objetivos_profissionais='',
                    sexo='1',
                    deficiencia='0',
                    telefone='19 9999-9999',
                    celular='19 9999-9999',
                    telefone_recado='19 9999-9999'
                    )
        self.resp = self.client.post(r(view_in_test), data)

    def test_atualizado_nome_completo(self):
        user = User.objects.get(username='eu@me.com')
        nome_completo = user.first_name
        self.assertEqual('Nome em Branco', nome_completo)

    def test_nao_atualizar_sobre_voce(self):
        user = User.objects.get(username='eu@me.com')
        armazenado = SobreMimModel.objects.get(user=user)
        self.assertEqual('Sou uma pessoa que...', armazenado.sobre_voce)

    def test_nao_atualizar_objetivos_profissionais(self):
        user = User.objects.get(username='eu@me.com')
        armazenado = SobreMimModel.objects.get(user=user)
        self.assertEqual('Meus objetivos profissionais são ...',
                         armazenado.objetivos_profissionais)

    def test_template(self):
        self.assertTemplateUsed(self.resp, template_in_test)

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SobreMimForm)
