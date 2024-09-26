import unittest
from ascii_art.fonts.py import get_available_fonts

class TestFonts(unittest.TestCase):
    def test_get_available_fonts(self):
        fonts = get_available_fonts()
        self.assertIsInstance(fonts, list)
        self.assertGreater(len(fonts), 0)

if __name__ == '__main__':
    unittest.main()