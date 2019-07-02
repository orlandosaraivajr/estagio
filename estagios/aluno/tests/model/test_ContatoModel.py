from datetime import datetime

from django.test import TestCase

from estagios.aluno.models import (
    CHOICES_ESTADOS_BRASILEIROS, ContatoModel)
from estagios.aluno.tests.model.test_SobreMimModel import userBuilder


class ContatoModelTest(TestCase):
    def setUp(self):
        self.user = userBuilder()
        self.cadastro = ContatoModel(
            user=self.user,
            endereco='Rua XYZ',
            endereco_numero='150',
            endereco_cidade='Rio Claro',
        )
        self.cadastro.save()

    def test_created(self):
        self.assertTrue(ContatoModel.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.cadastro.criado_em, datetime)

    def test_modified_at(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)

    def test_celular_padrao(self):
        celular = self.cadastro.celular
        self.assertEqual(celular, '')

    def test_telefone_padrao(self):
        telefone = self.cadastro.telefone
        self.assertEqual(telefone, '')

    def test_telefone_recado_padrao(self):
        telefone_recado = self.cadastro.telefone_recado
        self.assertEqual(telefone_recado, '')

    def test_endereco(self):
        endereco = self.cadastro.endereco
        self.assertEqual(endereco, 'Rua XYZ')

    def test_endereco_numero(self):
        endereco_numero = self.cadastro.endereco_numero
        self.assertEqual(endereco_numero, '150')

    def test_endereco_complemento(self):
        endereco_complemento = self.cadastro.endereco_complemento
        self.assertEqual(endereco_complemento, '')

    def test_endereco_complemento(self):
        endereco_complemento = self.cadastro.endereco_complemento
        self.assertEqual(endereco_complemento, '')

    def test_estado_padrao(self):
        estado = dict(CHOICES_ESTADOS_BRASILEIROS)[self.cadastro.endereco_estado]
        self.assertEqual(estado, 'São Paulo')

    def test_usuario_estudante(self):
        self.assertTrue(self.user.is_student)

    def test_usuario_nao_eh_professor(self):
        self.assertFalse(self.user.is_teacher)

    def test_usuario_nao_eh_empresa(self):
        self.assertFalse(self.user.is_worker)
