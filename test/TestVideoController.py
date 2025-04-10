import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.VideoController import VideoController
from src.Video import Video

class TestVideoPersonDetection(unittest.TestCase):

    def setUp(self):
        self.controller = VideoController()
        self.video_with_people = Video("test/Video con personas test.mp4")
        self.video_without_people = Video("test/Video test sin personas.mp4")

    def test_video_with_people_detected(self):
        people_by_frame, processed_video = self.controller.count_people_frontal(self.video_with_people)

        # Verifica si hay al menos un frame con personas
        people_detected = any(count > 0 for _, count in people_by_frame)
        self.assertTrue(people_detected, "Se esperaba detección de personas, pero no se encontró ninguna.")

        # Verifica que el vídeo procesado exista
        self.assertTrue(os.path.exists(processed_video.getPath()), "El vídeo procesado no se ha guardado correctamente.")

    def test_video_without_people_detected(self):
        people_by_frame, processed_video = self.controller.count_people_frontal(self.video_without_people)

        # Verifica que todos los frames tengan conteo cero
        all_frames_empty = all(count == 0 for _, count in people_by_frame)
        self.assertTrue(all_frames_empty, "No se esperaban personas, pero se detectó al menos una.")

        # Verifica que el vídeo procesado exista
        self.assertTrue(os.path.exists(processed_video.getPath()), "El vídeo procesado no se ha guardado correctamente.")

if __name__ == "__main__":
    unittest.main()
