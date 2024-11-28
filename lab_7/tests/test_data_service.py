import unittest
from unittest.mock import MagicMock
from bll.data_service import DataService
from dal.api_repository import APIRepository

class TestDataService(unittest.TestCase):
    def setUp(self):
        self.mock_repository = MagicMock(spec=APIRepository)
        self.service = DataService(self.mock_repository)

    def test_fetch_and_display_data(self):
        self.mock_repository.get_data.return_value = [{'id': 1, 'title': 'Test Post'}]
        data = self.service.fetch_and_display_data('posts')

        self.mock_repository.get_data.assert_called_once_with('posts')
        self.assertEqual(data[0]['title'], 'Test Post')

    def test_save_data_json(self):
        data = [{'id': 1, 'title': 'Test Post'}]
        self.service.save_data(data, 'json', 'output.json')

        self.mock_repository.save_as_json.assert_called_once_with(data, 'output.json')

    def test_save_data_csv(self):
        data = [{'id': 1, 'title': 'Test Post'}]
        self.service.save_data(data, 'csv', 'output.csv')

        self.mock_repository.save_as_csv.assert_called_once_with(data, 'output.csv')

    def test_save_data_invalid_format(self):
        data = [{'id': 1, 'title': 'Test Post'}]
        with self.assertRaises(ValueError):
            self.service.save_data(data, 'xml', 'output.xml')

if __name__ == '__main__':
    unittest.main()
