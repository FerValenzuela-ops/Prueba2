from django.test import TestCase

# Create your tests here.
class TestValidarRut(TestCase) :
    def test_rut(self) :
        rut = "191628686-3"
        resultado = validar_rut(rut)

