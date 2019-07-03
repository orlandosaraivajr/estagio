from django.db.models import QuerySet
from django.shortcuts import resolve_url as r
from django.test import Client, TestCase
from django.utils import timezone

from estagios.aluno.models import FaculdadeModel
from estagios.core.functions import registro_novo_aluno
from estagios.core.models import User

view_in_test = 'aluno:aluno_faculdade_excluir'
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


class AlunoPostOK(TestCase):
    def setUp(self):
        registro_novo_aluno('eu@me.com', '123')
        self.user = User.objects.get(username='eu@me.com')
        self.client = Client()
        self.client.login(username='eu@me.com', password='123')
        self.data = dict(chave_primaria=1)
        self.cadastro = FaculdadeModel(
            user=self.user,
            data_inicio=timezone.now(),
            curso='nome_do_curso',
            instituicao='fho',
        )
        self.cadastro.save()
        self.resp = self.client.post(r(view_in_test), self.data)

    def test_droped(self):
        self.assertFalse(FaculdadeModel.objects.exists())

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'aluno_faculdade.html')

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)


class AlunoPost_duas_faculdades_um_usuario(TestCase):
    def setUp(self):
        registro_novo_aluno('eu@me.com', '123')
        self.user = User.objects.get(username='eu@me.com')
        self.client = Client()
        self.client.login(username='eu@me.com', password='123')
        self.cadastro = FaculdadeModel(
            user=self.user,
            data_inicio=timezone.now(),
            curso='nome_do_curso',
            instituicao='fho',
        )
        self.cadastro.save()
        self.cadastro = FaculdadeModel(
            user=self.user,
            data_inicio=timezone.now(),
            curso='nome_do_curso_2',
            instituicao='fho',
        )
        self.cadastro.save()
        self.data = dict(chave_primaria=1)
        self.resp = self.client.post(r(view_in_test), self.data)

    def test_created(self):
        self.assertTrue(FaculdadeModel.objects.exists())

    def test_querySet(self):
        form = self.resp.context['faculdades']
        self.assertIsInstance(form, QuerySet)

    def test_um_querySet(self):
        query_set = self.resp.context['faculdades']
        self.assertEqual(len(query_set), 1)


class AlunoPost_duas_faculdades_dois_usuarios(TestCase):
    def setUp(self):
        registro_novo_aluno('eu@me.com', '123')
        self.user = User.objects.get(username='eu@me.com')
        self.client = Client()
        self.client.login(username='eu@me.com', password='123')
        self.cadastro = FaculdadeModel(
            user=self.user,
            data_inicio=timezone.now(),
            curso='nome_do_curso',
            instituicao='fho',
        )
        self.cadastro.save()
        registro_novo_aluno('eu2@me.com', '1234')
        self.user = User.objects.get(username='eu2@me.com')
        self.client.login(username='eu2@me.com', password='1234')
        self.cadastro = FaculdadeModel(
            user=self.user,
            data_inicio=timezone.now(),
            curso='nome_do_curso_2',
            instituicao='fho',
        )
        self.cadastro.save()
        self.data = dict(chave_primaria=2)
        self.resp = self.client.post(r(view_in_test), self.data)

    def test_created(self):
        self.assertTrue(FaculdadeModel.objects.exists())

    def test_querySet(self):
        query_set = self.resp.context['faculdades']
        self.assertIsInstance(query_set, QuerySet)

    def test_um_querySet(self):
        query_set = self.resp.context['faculdades']
        self.assertEqual(len(query_set), 0)
