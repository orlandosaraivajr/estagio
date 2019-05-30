from django.test import TestCase
from django.shortcuts import resolve_url as r

class coreGetHome(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:core_home'))

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_200_template_home(self):
        self.assertEqual(200, self.resp.status_code)
