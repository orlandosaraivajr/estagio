from django.shortcuts import resolve_url as r
from django.test import Client, TestCase

from estagios.core.models import User

view_in_test = 'aluno:aluno_home'
template_in_test = 'aluno_index.html'


class AlunoGet(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            'admin',
            'admin@admin.com',
            '123',
            is_student=True)
        self.client.login(username='admin', password='123')
        self.resp = self.client.get(r(view_in_test))

    def test_template(self):
        self.assertTemplateUsed(self.resp, template_in_test)

    def test_200_template(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html_template(self):
        tags = (
            ('Start Bootstrap', 1),
            ('Dashboard', 2),
            ('Charts', 1),
            ('New Messages!', 1),
            ('New Tasks!', 1)
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
