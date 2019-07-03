from django.shortcuts import resolve_url as r
from django.test import Client, TestCase
from django.utils import timezone

from estagios.aluno.models import FaculdadeModel
from estagios.core.functions import registro_novo_aluno
from estagios.core.models import User

view_in_test = 'aluno:aluno_faculdade_editar'
template_in_test = 'aluno_faculdade_editar.html'


class AlunoGet(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            'admin',
            'eu@me.com',
            '123',
            is_student=True)
        self.client.login(username='admin', password='123')
        self.resp = self.client.get(r(view_in_test))

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'aluno_faculdade.html')

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html_template(self):
        tags = (
            ('Estágio Nota 10', 2),
            ('Contato', 1),
            ('Faculdade', 2),
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
        self.user = User.objects.get(username='eu@me.com')
        self.client = Client()
        self.client.login(username='eu@me.com', password='123')
        self.data = dict(data_inicio='12/12/2019',
                         data_fim='02/02/2020',
                         curso='novo_curso',
                         instituicao='nova_instituição',
                         situacao='1',carga_horaria='3600',
                         chave_primaria=1,
                         )
        self.cadastro = FaculdadeModel(
            user=self.user,
            data_inicio=timezone.now(),
            curso='nome_do_curso',
            instituicao='fho',
        )
        self.cadastro.save()
        self.resp = self.client.post(r(view_in_test), self.data)

    def test_created(self):
        self.assertTrue(FaculdadeModel.objects.exists())

    def test_nome_curso(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertEqual(self.data['curso'], armazenado.curso)

    def test_instituicao(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertEqual(self.data['instituicao'], armazenado.instituicao)

    def test_situacao(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertEqual(self.data['situacao'], armazenado.situacao)

    def test_carga_horaria(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertEqual(int(self.data['carga_horaria']), armazenado.carga_horaria)

    def test_data_inicio(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertEqual(12, armazenado.data_inicio.month)
        self.assertEqual(12, armazenado.data_inicio.day)
        self.assertEqual(2019, armazenado.data_inicio.year)

    def test_data_fim(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertEqual(2, armazenado.data_fim.month)
        self.assertEqual(2, armazenado.data_fim.day)
        self.assertEqual(2020, armazenado.data_fim.year)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'aluno_faculdade.html')

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)


class AlunoPostFail_error_in_pk(TestCase):
    '''pk=2, Não existe objeto no banco de dados'''

    def setUp(self):
        registro_novo_aluno('eu@me.com', '123')
        self.user = User.objects.get(username='eu@me.com')
        self.client = Client()
        self.client.login(username='eu@me.com', password='123')
        self.data = dict(data_inicio='3/3/2018',
                         data_fim='12/08/2018',
                         curso='novo_curso',
                         instituicao='nova_instituição',
                         situacao='1',
                         carga_horaria='3600',
                         chave_primaria=2,
                         )
        self.cadastro = FaculdadeModel(
            user=self.user,
            data_inicio=timezone.now(),
            curso='nome_do_curso',
            instituicao='fho',
        )
        self.cadastro.save()
        self.resp = self.client.post(r(view_in_test), self.data)

    def test_created(self):
        self.assertTrue(FaculdadeModel.objects.exists())

    def test_nome_curso(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertNotEqual(self.data['curso'], armazenado.curso)

    def test_instituicao(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertNotEqual(self.data['instituicao'], armazenado.instituicao)

    def test_situacao(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertNotEqual(self.data['situacao'], armazenado.situacao)

    def test_carga_horaria(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertNotEqual(int(self.data['carga_horaria']), armazenado.carga_horaria)

    def test_data_inicio(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertNotEqual(2018, armazenado.data_inicio.year)

    def test_data_fim(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertNotEqual(2018, armazenado.data_fim.year)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'aluno_faculdade.html')

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)


class AlunoPostFail_error_in_form(TestCase):
    def setUp(self):
        registro_novo_aluno('eu@me.com', '123')
        self.user = User.objects.get(username='eu@me.com')
        self.client = Client()
        self.client.login(username='eu@me.com', password='123')
        self.data = dict(data_inicio='3/3/2018',
                         data_fim='12/08/2018',
                         instituicao='nova_instituição',
                         situacao='1',
                         carga_horaria='3600',
                         chave_primaria=1,
                         )
        self.cadastro = FaculdadeModel(
            user=self.user,
            data_inicio=timezone.now(),
            curso='nome_do_curso',
            instituicao='fho',
        )
        self.cadastro.save()
        self.resp = self.client.post(r(view_in_test), self.data)

    def test_created(self):
        self.assertTrue(FaculdadeModel.objects.exists())

    def test_nome_curso(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertEqual('nome_do_curso', armazenado.curso)

    def test_instituicao(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertNotEqual(self.data['instituicao'], armazenado.instituicao)

    def test_situacao(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertNotEqual(self.data['situacao'], armazenado.situacao)

    def test_carga_horaria(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertNotEqual(int(self.data['carga_horaria']), armazenado.carga_horaria)

    def test_data_inicio(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertNotEqual(2018, armazenado.data_inicio.year)

    def test_data_fim(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertNotEqual(2018, armazenado.data_fim.year)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'aluno_faculdade.html')

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)
