from datetime import datetime

import pytz

from django.test import TestCase

from estagios.aluno.models import CadastroModel, CHOICES_DEFICIENCIA, CHOICES_SEXO, ContatoModel, \
    CHOICES_ESTADOS_BRASILEIROS
from estagios.core.models import User


def userBuilder():
    return User.objects.create_user(
        username='orlandosaraivajr',
        email='orlandosaraivajr@gmail.com',
        password='segredo',
        first_name='Orlando',
        last_name='Saraiva Jr',
    )

class CadastroModelTest(TestCase):
    def setUp(self):
        self.user = userBuilder()
        self.nascimento = datetime(1981, 12, 30, 10, 20, 10, 127325, tzinfo=pytz.UTC)
        self.cadastro = CadastroModel(
            user=self.user,
            data_nascimento = self.nascimento,
            sobre_voce = 'O melhor profissional do mundo',
            objetivos_profissionais = 'Quero dominar o mundo',
        )
        self.cadastro.save()

    def test_created(self):
        self.assertTrue(CadastroModel.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.cadastro.criado_em , datetime)

    def test_modified_at(self):
        self.assertIsInstance(self.cadastro.modificado_em , datetime)

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

    def test_telefone_padrao(self):
        telefone = self.cadastro.telefone
        self.assertEqual(telefone, '')

    def test_celular_padrao(self):
        celular = self.cadastro.celular
        self.assertEqual(celular, '')

    def test_telefone_recado_padrao(self):
        telefone_recado = self.cadastro.telefone_recado
        self.assertEqual(telefone_recado, '')

    def test_usuario_estudante(self):
        self.assertTrue(self.user.is_student)

    def test_usuario_nao_eh_professor(self):
        self.assertFalse(self.user.is_teacher)

    def test_usuario_nao_eh_empresa(self):
        self.assertFalse(self.user.is_worker)

class ContatoModelTest(TestCase):
    def setUp(self):
        self.user = userBuilder()
        self.cadastro = ContatoModel(
            user=self.user,
            github="https://github.com/orlandosaraivajr",
            linkedin="http://www.linkedIn.com",
            facebook="http://www.facebook.com.br",
            endereco='Rua XYZ',
            endereco_numero = '150',
            # endereco_complemento = '',
            endereco_cidade = 'Rio Claro',
            # endereco_estado = 'SP',

        )
        self.cadastro.save()

    def test_created(self):
        self.assertTrue(ContatoModel.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.cadastro.criado_em , datetime)

    def test_modified_at(self):
        self.assertIsInstance(self.cadastro.modificado_em , datetime)

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