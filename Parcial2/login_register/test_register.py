import unittest

class TestContraseniaDistinta(unittest.TestCase):
    def test_negativo(self):
        contra1 = "1234"
        contra2 = "1234"
        mensaje = "La primera contraseña y la segunda contraseña son iguales!"

        self.assertEqual(contra1,contra2,mensaje)

if __name__ == '__main__':
    unittest.main()