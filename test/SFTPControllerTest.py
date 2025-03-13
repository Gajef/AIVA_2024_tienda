import unittest
from src.SFTPController import SFTPController

class SFTPControllerTest(unittest.TestCase):

    def setUp(self):
        self.sftp = SFTPController()

    def test_retrieve_last_video(self):
        video = self.sftp.retrieve_last_video()
        self.assertIsNotNone(video)

    def test__connect(self):
        connection = self.sftp._connect()
        self.assertIsNotNone(connection)

if __name__ == '__main__':
    unittest.main()
