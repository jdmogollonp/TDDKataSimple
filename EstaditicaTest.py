from unittest import TestCase
from Estadistica import Estadistica

class EstaditicaTest(TestCase):
    def test_procesar_secuencia(self):
        self.assertEqual(Estadistica().procesar_secuencia(""),[0, None, None, None],"Cadena vacio")

    def test_procesar_secuencia_cadenaConUnNumero(self):
        self.assertEqual(Estadistica().procesar_secuencia("2"), [1, 2, 2, 2], "Un numero")

    def test_procesar_secuencia_cadenaConDosNumeros(self):
        self.assertEqual(Estadistica().procesar_secuencia("1,3"), [2, 1, 3, 2], "Dos numeros")

    def test_procesar_secuencia_cadenaConMultiplesNumeros(self):
        self.assertEqual(Estadistica().procesar_secuencia("5,2,4,7"), [4, 2, 7, 4.5], "Multiples numeros")