from datetime import datetime

import pytz
from django.shortcuts import resolve_url as r
from django.test import Client, TestCase

from estagios.aluno.models import CadastroModel
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
        cadastro = CadastroModel()
        cadastro.user = User.objects.get(email='eu@me.com')
        cadastro.data_nascimento = datetime(2000, 1, 1, 0, 0, 0, tzinfo=pytz.UTC)
        cadastro.save()
        self.client.login(username='eu@me.com', password='123')
        self.resp = self.client.get(r(view_in_test))

    def test_template(self):
        self.assertTemplateUsed(self.resp, template_in_test)

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html_template(self):
        tags = (
            ('Estágio Nota 10', 2),
            ('Contato', 1),
            ('Faculdade', 1),
            ('Outros cursos', 1),
            ('Empregos Anteriores', 1),
            ('Sair', 3)
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


