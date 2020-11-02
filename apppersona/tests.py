from django.http import response
from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse
#from .validador_rut import validar_rut

class TestUrls(SimpleTestCase):
    def test_inicio_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_inicio_url_nombre(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'apppersona/index.html')


# Create your tests here.

