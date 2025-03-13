import unittest
from src.DeleteVideosController import DeleteVideosController

class TestDeleteVideosController(unittest.TestCase):
    def test_delete_videos(self):
        # Arrange: Crear una instancia de DeleteVideosController y definir una ruta de videos de prueba
        controller = DeleteVideosController()
        videos_path = "ruta/a/los/videos"  # Datos de ejemplo

        # Act: Llamar al método delete_videos
        resultado = controller.delete_videos(videos_path)

        # Assert: Comprobar que el resultado es exactamente "Eliminados"
        self.assertEqual(resultado, "Eliminados", "La función delete_videos debería retornar 'Eliminados'.")

if __name__ == '__main__':
    unittest.main()
