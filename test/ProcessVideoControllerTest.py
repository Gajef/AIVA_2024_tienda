import unittest
from src.ProcessVideoController import ProcessVideoController

class TestProcessVideoController(unittest.TestCase):
    def test_count_people(self):
        # Arrange: Crear una instancia de ProcessVideoController y definir un video de prueba
        controller = ProcessVideoController()
        video = "video_de_prueba"  # Datos de ejemplo, puede ser un string o el tipo de dato que uses para videos

        # Act: Llamar al metodo count_people
        resultado = controller.count_people(video)

        # Assert: Comprobar que el resultado es exactamente "Finalizado"
        self.assertEqual(resultado, "Finalizado", "La función count_people debería retornar 'Finalizado'.")

if __name__ == '__main__':
    unittest.main()
