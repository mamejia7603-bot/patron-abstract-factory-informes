import unittest

from procesador import ProcesadorInformes
from productos import (CompraEntrada, CompraMixta, CompraSalida, FacturaEntrada,
                       FacturaMixta, FacturaSalida)


class TestProcesadorMixta(unittest.TestCase):
    def setUp(self):
        self.procesador = ProcesadorInformes()

    def test_crea_el_informe_correcto(self):
        casos = {
            "ENT_FAC_001.txt": FacturaEntrada,
            "ENT_COM_001.txt": CompraEntrada,
            "SAL_FAC_001.txt": FacturaSalida,
            "SAL_COM_001.txt": CompraSalida,
            "MIX_FAC_001.txt": FacturaMixta,
            "MIX_COM_001.txt": CompraMixta,
        }
        for nombre, clase in casos.items():
            with self.subTest(nombre=nombre):
                self.assertIsInstance(self.procesador.obtener_informe(nombre), clase)

    def test_mensaje_indica_categoria_y_tipo(self):
        mensaje = self.procesador.obtener_informe("SAL_COM_001.txt").procesar("SAL_COM_001.txt")
        self.assertIn("Procesando informe de SALIDA de tipo COMPRA", mensaje)

    def test_nombres_invalidos(self):
        for nombre in ["XYZ_FAC_001.txt", "ENT_XXX_001.txt", "ENT_FAC.txt", "ENT_FAC_001.pdf"]:
            with self.subTest(nombre=nombre):
                with self.assertRaises(ValueError):
                    self.procesador.obtener_informe(nombre)


if __name__ == "__main__":
    unittest.main()
