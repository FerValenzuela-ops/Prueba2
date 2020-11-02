from django.http import response
from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse
from .forms import FormularioPersona
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

class TestForms(SimpleTestCase):
    def test_form_valid_data(self):
        form = FormularioPersona(data={
            'nombre': 'nombre1',
            'apellido': 'apellido1',
            'email': 'nombre@gmail.com',
            'celular': '12345678',
            'region': 'rm'
        })
        self.assertTrue(form.is_valid())
    
    def test_no_data(self):
        form = FormularioPersona(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

# Create your tests here.

