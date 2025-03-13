import unittest
from src.EmailController import EmailController

class EmailControllerTest(unittest.TestCase):

    def setUp(self):
        self.emailController = EmailController()

    def test_send_email(self):
        response = self.emailController.send_email("", "", "")
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
