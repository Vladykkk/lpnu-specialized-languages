import unittest
from ascii_art.colors import get_available_colors

class TestColors(unittest.TestCase):
    def test_get_available_colors(self):
        colors = get_available_colors()
        self.assertIsInstance(colors, list)
        self.assertGreater(len(colors), 0)

if __name__ == '__main__':
    unittest.main()