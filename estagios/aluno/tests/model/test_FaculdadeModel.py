from datetime import datetime

from django.test import TestCase
from django.utils import timezone

from estagios.aluno.models import (
    FaculdadeModel, CHOICES_SITUACAO_ACADEMICA)
from estagios.aluno.tests.model.test_SobreMimModel import userBuilder


class FaculdadeModelTest(TestCase):
    def setUp(self):
        self.user = userBuilder()
        self.inicio = timezone.now()
        self.cadastro = FaculdadeModel(
            user=self.user,
            data_inicio=self.inicio,
            curso='nome_do_curso',
            instituicao='fho',
        )
        self.cadastro.save()

    def test_created(self):
        self.assertTrue(FaculdadeModel.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.cadastro.criado_em, datetime)

    def test_modified_at(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)

    def test_data_inicio(self):
        inicio = self.cadastro.data_inicio
        self.assertEqual(inicio, self.inicio)

    def test_data_fim(self):
        armazenado = self.cadastro.data_fim
        fim = self.cadastro.data_com_acrescido()
        self.assertEqual(fim.year, armazenado.year)
        self.assertEqual(fim.month, armazenado.month)
        self.assertEqual(fim.day, armazenado.day)

    def test_curso(self):
        self.assertEqual(self.cadastro.curso, 'nome_do_curso')

    def test_carga_horaria(self):
        self.assertEqual(self.cadastro.carga_horaria, '2400')

    def test_instituicao(self):
        self.assertEqual(self.cadastro.instituicao, 'fho')

    def test_situacao_padrao(self):
        situacao = dict(CHOICES_SITUACAO_ACADEMICA)[self.cadastro.situacao]
        self.assertEqual(situacao, 'em andamento')

    def test_usuario_estudante(self):
        self.assertTrue(self.user.is_student)

    def test_usuario_nao_eh_professor(self):
        self.assertFalse(self.user.is_teacher)

    def test_usuario_nao_eh_empresa(self):
        self.assertFalse(self.user.is_worker)
