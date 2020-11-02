from django.test import TestCase
from .validador_rut import validar_rut

class TestUrls(TestCase):
    def test_list(self):
        assert 1 == 2



# Create your tests here.
class TestValidarRut(TestCase) :
    def test_rut(self) :
        rut = "191628686-3"
        resultado = validar_rut(rut)
        self.assertTrue(resultado)

    def test_rut_invalido(self) :
        rut = "191628686-4"
        resultado = validar_rut(rut)
        self.assertFalse(resultado)
