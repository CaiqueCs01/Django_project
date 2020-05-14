from django.test import TestCase
from Pizza.models import CadConsumidor


class CadConsumidorTest(TestCase):
    def setUp(self):
        CadConsumidor.objects.create(nome="Rambo", endereço="rua dos bobo")
        CadConsumidor.objects.create(nome="Stalone", endereço="rua dos bobo2")

    def test_registro_esta_salvando(self):
        """Teste para saber se a view Registro está salvando certo"""
        rambo = CadConsumidor.objects.get(nome="Rambo")
        stalone = CadConsumidor.objects.get(nome="Stalone")
        self.assertEqual(rambo.email(), 'The lion says "rambo@gmail.com"')
        self.assertEqual(stalone.email(), 'The cat says "stalone@gmail.com"')
