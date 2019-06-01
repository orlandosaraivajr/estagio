from django.test import TestCase
from django.shortcuts import resolve_url as r

class alunoGetHome(TestCase):
    def setUp(self):
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
            ('New Tasks!', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

class alunoGetCadastro(TestCase):
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