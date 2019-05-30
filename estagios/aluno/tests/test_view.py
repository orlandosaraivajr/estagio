from django.test import TestCase
from django.shortcuts import resolve_url as r

class alunoGetHome(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('aluno:aluno_home'))

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'aluno_index.html')

    def test_200_template_home(self):
        self.assertEqual(200, self.resp.status_code)
