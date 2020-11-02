from django.http import response
from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse
from .forms import FormularioPersona # Import del formulario desde el forms

# Pruebas Unitarias de urls
class TestUrls(SimpleTestCase):
    # Prueba del code del url 
    def test_inicio_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    # Prueba del nomre de la url
    def test_inicio_url_nombre(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    # Prueba del template de la url
    def test_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'apppersona/index.html')

# Pruebas unitarias del formulario
class TestForms(SimpleTestCase):
    # Prueba de validacion de datos
    def test_form_valid_data(self):
        form = FormularioPersona(data={
            'nombre': 'nombre1',
            'apellido': 'apellido1',
            'email': 'nombre1@gmail.com',
            'celular': '12345678',
            'region': 'rm',
            'rut': '123456789'
        })
        self.assertTrue(form.is_valid())

    # Prueba de validacion de formulario vacio
    def test_no_data(self):
        form = FormularioPersona(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

