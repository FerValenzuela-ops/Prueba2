from django.http import response
from django.test import TestCase, SimpleTestCase
#from .validador_rut import validar_rut

class TestUrls(SimpleTestCase):
    def test_inicio(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)



# Create your tests here.

