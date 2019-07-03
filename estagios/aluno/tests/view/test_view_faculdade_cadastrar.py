from django.db.models import QuerySet
from django.shortcuts import resolve_url as r
from django.test import Client, TestCase

from estagios.aluno.forms import FaculdadeForm
from estagios.aluno.models import FaculdadeModel
from estagios.core.functions import registro_novo_aluno
from estagios.core.models import User

view_in_test = 'aluno:aluno_faculdade_cadastro'
template_in_test = 'aluno_faculdade_cadastrar.html'


class AlunoGet(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user('admin', 'eu@me.com', '123', is_student=True)
        self.client.login(username='admin', password='123')
        self.resp = self.client.get(r(view_in_test))

    def test_template(self):
        self.assertTemplateUsed(self.resp, template_in_test)

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html_template(self):
        tags = (
            ('Estágio Nota 10', 2),
            ('Contato', 1),
            ('Faculdade', 3),
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
        self.client = Client()
        self.client.login(username='eu@me.com', password='123')
        self.data = dict(data_inicio='01/12/2019',
                         data_fim='02/11/2020',
                         curso='nome_do_curso',
                         instituicao='fho',
                         situacao='0',
                         carga_horaria='2400',
                         )
        self.resp = self.client.post(r(view_in_test), self.data)
        self.user = User.objects.get(username='eu@me.com')

    def test_created(self):
        self.assertTrue(FaculdadeModel.objects.exists())

    def test_data_inicio(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertEqual(12, armazenado.data_inicio.month)
        self.assertEqual(1, armazenado.data_inicio.day)
        self.assertEqual(2019, armazenado.data_inicio.year)

    def test_data_fim(self):
        armazenado = FaculdadeModel.objects.get(user=self.user)
        self.assertEqual(11, armazenado.data_fim.month)
        self.assertEqual(2, armazenado.data_fim.day)
        self.assertEqual(2020, armazenado.data_fim.year)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'aluno_faculdade.html')

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_querySet(self):
        query_set = self.resp.context['faculdades']
        self.assertIsInstance(query_set, QuerySet)


class AlunoPostFail(TestCase):
    def setUp(self):
        registro_novo_aluno('eu@me.com', '123')
        self.client = Client()
        self.client.login(username='eu@me.com', password='123')
        self.data = {}
        self.resp = self.client.post(r(view_in_test), self.data)
        self.user = User.objects.get(username='eu@me.com')

    def test_created(self):
        self.assertFalse(FaculdadeModel.objects.exists())

    def test_template(self):
        self.assertTemplateUsed(self.resp, template_in_test)

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, FaculdadeForm)


class AlunoPost_duas_faculdades_um_usuario(TestCase):
    def setUp(self):
        registro_novo_aluno('eu@me.com', '123')
        self.client = Client()
        self.client.login(username='eu@me.com', password='123')
        self.data1 = dict(data_inicio='01/01/2001', data_fim='02/11/2005',
                         curso='nome_do_curso_1', instituicao='fho',
                         situacao='0', carga_horaria='2400')
        self.resp = self.client.post(r(view_in_test), self.data1)
        self.data2 = dict(data_inicio='01/01/2006', data_fim='02/11/2009',
                         curso='nome_do_curso_2', instituicao='fho',
                         situacao='0', carga_horaria='2400')
        self.resp = self.client.post(r(view_in_test), self.data2)

    def test_created(self):
        self.assertTrue(FaculdadeModel.objects.exists())

    def test_querySet(self):
        form = self.resp.context['faculdades']
        self.assertIsInstance(form, QuerySet)

    def test_dois_querySets(self):
        query_set = self.resp.context['faculdades']
        self.assertEqual(len(query_set), 2)

class AlunoPost_duas_faculdades_dois_usuarios(TestCase):
    def setUp(self):
        registro_novo_aluno('eu@me.com', '123')
        registro_novo_aluno('eu2@me.com', '1234')
        self.client = Client()
        self.client.login(username='eu@me.com', password='123')
        self.data1 = dict(data_inicio='01/01/2001', data_fim='02/11/2005',
                         curso='nome_do_curso_1', instituicao='fho',
                         situacao='0', carga_horaria='2400')
        self.resp = self.client.post(r(view_in_test), self.data1)
        self.client.login(username='eu2@me.com', password='1234')
        self.data2 = dict(data_inicio='01/01/2006', data_fim='02/11/2009',
                         curso='nome_do_curso_2', instituicao='fho',
                         situacao='0', carga_horaria='2400')
        self.resp = self.client.post(r(view_in_test), self.data2)
        self.user = User.objects.get(username='eu2@me.com')

    def test_created(self):
        self.assertTrue(FaculdadeModel.objects.exists())

    def test_querySet(self):
        query_set = self.resp.context['faculdades']
        self.assertIsInstance(query_set, QuerySet)

    def test_um_querySet(self):
        query_set = self.resp.context['faculdades']
        self.assertEqual(len(query_set), 1)