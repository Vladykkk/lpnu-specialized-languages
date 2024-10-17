import unittest
from unittest.mock import patch
from dal.api_repository import APIRepository

class TestAPIRepository(unittest.TestCase):

    @patch('dal.api_repository.requests.get')
    def test_get_data_failure(self, mock_get):
        mock_get.side_effect = Exception("API Error")
        
        repository = APIRepository("https://jsonplaceholder.typicode.com")
        
        with self.assertRaises(Exception) as context:
            repository.get_data("invalid")
    
        self.assertEqual(str(context.exception), "API Error")

if __name__ == '__main__':
    unittest.main()
