import unittest
from src.VideoController import VideoController

class TestProcessVideoController(unittest.TestCase):
    def test_count_people(self):
        # Arrange: Crear una instancia de VideoController y definir un video de prueba
        controller = VideoController()
        video = "video_de_prueba"  # Datos de ejemplo, puede ser un string o el tipo de dato que uses para videos

        # Act: Llamar al metodo count_people
        resultado = controller.count_people(video)

        # Assert: Comprobar que el resultado es exactamente "Finalizado"
        self.assertEqual(resultado, "Finalizado", "La función count_people debería retornar 'Finalizado'.")

    def test_delete_videos(self):
        # Arrange: Crear una instancia de DeleteVideosController y definir una ruta de videos de prueba
        controller = VideoController()
        videos_path = "ruta/a/los/videos"  # Datos de ejemplo

        # Act: Llamar al metodo delete_videos
        resultado = controller.delete_videos(videos_path)

        # Assert: Comprobar que el resultado es exactamente "Eliminados"
        self.assertEqual(resultado, "Eliminados", "La función delete_videos debería retornar 'Eliminados'.")

if __name__ == '__main__':
    unittest.main()
