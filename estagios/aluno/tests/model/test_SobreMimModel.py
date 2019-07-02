from datetime import datetime

from django.test import TestCase
from django.utils import timezone

from estagios.aluno.models import (
    CHOICES_DEFICIENCIA, CHOICES_SEXO, SobreMimModel)
from estagios.core.models import User


def userBuilder():
    return User.objects.create_user(
        username='orlandosaraivajr',
        email='orlandosaraivajr@gmail.com',
        password='segredo',
        first_name='Orlando',
        last_name='Saraiva Jr',
    )


class SobreMimModelTest(TestCase):
    def setUp(self):
        self.user = userBuilder()
        self.nascimento = timezone.now()
        self.cadastro = SobreMimModel(
            user=self.user,
            data_nascimento=self.nascimento,
            sobre_voce='O melhor profissional do mundo',
            objetivos_profissionais='Quero dominar o mundo',
        )
        self.cadastro.save()

    def test_created(self):
        self.assertTrue(SobreMimModel.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.cadastro.criado_em, datetime)

    def test_modified_at(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)

    def test_data_nascimento(self):
        data_nascimento = self.cadastro.data_nascimento
        self.assertEqual(data_nascimento, self.nascimento)

    def test_sobre_voce(self):
        sobre_voce = self.cadastro.sobre_voce
        self.assertEqual(sobre_voce, 'O melhor profissional do mundo')

    def test_objetivos_profissionais(self):
        objetivos = self.cadastro.objetivos_profissionais
        self.assertEqual(objetivos, 'Quero dominar o mundo')

    def test_deficiencia_padrao(self):
        deficiencia = dict(CHOICES_DEFICIENCIA)[self.cadastro.deficiencia]
        self.assertEqual(deficiencia, 'NENHUMA')

    def test_sexo_padrao(self):
        sexo = dict(CHOICES_SEXO)[self.cadastro.sexo]
        self.assertEqual(sexo, 'MASCULINO')

    def test_usuario_estudante(self):
        self.assertTrue(self.user.is_student)

    def test_usuario_nao_eh_professor(self):
        self.assertFalse(self.user.is_teacher)

    def test_usuario_nao_eh_empresa(self):
        self.assertFalse(self.user.is_worker)
