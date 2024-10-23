import unittest
import json
from server import app

class TestServer(unittest.TestCase):

    def setUp(self):
        """Set up the test client."""
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        """Test the home page."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sous Vide Cooking Times', response.data)

    def test_get_times(self):
        """Test the /times endpoint."""
        response = self.app.get('/times?food_type=Apples')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIn('food_type', data[0])
        self.assertIn('temperature', data[0])
        self.assertIn('cooking_time', data[0])

    def test_get_food_types(self):
        """Test the /food_types endpoint."""
        response = self.app.get('/food_types?query=App')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIn('Apples', data)

if __name__ == '__main__':
    unittest.main()
