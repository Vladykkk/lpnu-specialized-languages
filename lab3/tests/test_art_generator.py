import unittest
from ascii_art.art_generator import generate_ascii_art, save_ascii_art, replace_symbols

class TestArtGenerator(unittest.TestCase):
    def test_generate_ascii_art(self):
        result = generate_ascii_art("Test")
        self.assertIn("Test", result)

    def test_generate_ascii_art_with_width(self):
        result = generate_ascii_art("Test", width=20)
        self.assertIn("Test", result)
        self.assertTrue(all(len(line) <= 20 for line in result.split('\n')))

    def test_generate_ascii_art_with_symbols(self):
        result = generate_ascii_art("Test", symbols='#*')
        self.assertIn('#', result)
        self.assertIn('*', result)

    def test_replace_symbols(self):
        ascii_art = " _|/\\"
        result = replace_symbols(ascii_art, '#*+-')
        self.assertEqual(result, "#*+-+")

    def test_save_ascii_art(self):
        ascii_art = generate_ascii_art("Test")
        save_ascii_art(ascii_art, "test_art.txt")
        with open("test_art.txt", "r") as file:
            content = file.read()
        self.assertEqual(content, ascii_art)

if __name__ == '__main__':
    unittest.main()