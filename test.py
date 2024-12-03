import unittest
import os

archivo_texto = "texto_guardado.txt"

def guardar_texto(texto):
    with open(archivo_texto, "w") as archivo:
        archivo.write(texto) 

def recuperar_texto():
    try:
        with open(archivo_texto, "r") as archivo:
            return archivo.read()  
    except FileNotFoundError:
        return ""

class TestFuncionesTexto(unittest.TestCase):

    def test_guardar_texto(self):

        texto_a_guardar = "Este es un texto de prueba"
        guardar_texto(texto_a_guardar)

        with open(archivo_texto, "r") as archivo:
            texto_recuperado = archivo.read()
            self.assertEqual(texto_recuperado, texto_a_guardar)

    def test_recuperar_texto(self):
        texto_a_guardar = "Texto para recuperar"
        guardar_texto(texto_a_guardar)

        texto_recuperado = recuperar_texto()

        self.assertEqual(texto_recuperado, texto_a_guardar)

    def test_recuperar_texto_vacio(self):
        if os.path.exists(archivo_texto):
            os.remove(archivo_texto) 

        texto_recuperado = recuperar_texto()

        self.assertEqual(texto_recuperado, "")

if __name__ == '__main__':
    unittest.main()
