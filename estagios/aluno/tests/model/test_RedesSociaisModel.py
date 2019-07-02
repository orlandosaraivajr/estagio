from datetime import datetime

from django.test import TestCase

from estagios.aluno.models import (
    RedesSociaisModel)
from estagios.aluno.tests.model.test_SobreMimModel import userBuilder


class RedesSociaisModelTest(TestCase):
    def setUp(self):
        self.user = userBuilder()
        self.cadastro = RedesSociaisModel(
            user=self.user,
            github="https://github.com/orlandosaraivajr",
            linkedin="http://www.linkedIn.com",
            facebook="http://www.facebook.com.br",
        )
        self.cadastro.save()

    def test_created(self):
        self.assertTrue(RedesSociaisModel.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.cadastro.criado_em, datetime)

    def test_modified_at(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)

    def test_github(self):
        github = self.cadastro.github
        self.assertEqual(github, 'https://github.com/orlandosaraivajr')

    def test_linkedin(self):
        linkedin = self.cadastro.linkedin
        self.assertEqual(linkedin, 'http://www.linkedIn.com')

    def test_facebook(self):
        facebook = self.cadastro.facebook
        self.assertEqual(facebook, 'http://www.facebook.com.br')

    def test_portfolio(self):
        portfolio = self.cadastro.portfolio
        self.assertEqual(portfolio, '')

    def test_usuario_estudante(self):
        self.assertTrue(self.user.is_student)

    def test_usuario_nao_eh_professor(self):
        self.assertFalse(self.user.is_teacher)

    def test_usuario_nao_eh_empresa(self):
        self.assertFalse(self.user.is_worker)
