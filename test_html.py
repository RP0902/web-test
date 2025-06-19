import os
import unittest
from bs4 import BeautifulSoup

HTML_FILES = [f for f in os.listdir('.') if f.endswith('.html')]

class TestHTML(unittest.TestCase):
    def test_no_replacement_characters(self):
        for fpath in HTML_FILES:
            with open(fpath, 'r', encoding='utf-8') as f:
                data = f.read()
            self.assertNotIn('\uFFFC', data, f"{fpath} contains unexpected character")
            self.assertNotIn('\uFFFD', data, f"{fpath} contains replacement character")

    def test_img_tags_have_alt(self):
        for fpath in HTML_FILES:
            with open(fpath, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
            for img in soup.find_all('img'):
                self.assertIn('alt', img.attrs, f"Image in {fpath} missing alt")
                self.assertTrue(img['alt'].strip(), f"Image in {fpath} has empty alt")

if __name__ == '__main__':
    unittest.main()
