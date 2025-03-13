import unittest
from src.CsvGeneratorController import CsvGeneratorController

class TestCsvGeneratorController(unittest.TestCase):
    def test_generate_csv(self):
        # Arrange: Crear una instancia de CsvGeneratorController y definir datos de prueba
        controller = CsvGeneratorController()
        inference_data = {"dato": "valor"}  # Datos de ejemplo

        # Act: Llamar al metodo generate csv
        resultado = controller.generate_csv(inference_data)

        # Assert: Comprobar que el resultado es exactamente "Generado"
        self.assertEqual(resultado, "Generado", "La función generate_csv debería retornar 'Generado'.")

if __name__ == '__main__':
    unittest.main()