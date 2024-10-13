import unittest
from src.ignore_parser import parse_ignore_file, is_ignored

class TestIgnoreParser(unittest.TestCase):
    def setUp(self):
        self.spec = parse_ignore_file('examples/example_gitignore')

    def test_ignored_file(self):
        self.assertTrue(is_ignored('venv/lib/python3.8/site-packages', self.spec))
        self.assertTrue(is_ignored('temp/data.txt', self.spec))

    def test_non_ignored_file(self):
        self.assertFalse(is_ignored('src/main.py', self.spec))
        self.assertFalse(is_ignored('README.md', self.spec))

if __name__ == '__main__':
    unittest.main()
