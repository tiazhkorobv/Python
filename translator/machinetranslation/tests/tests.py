''' Here are testcases for translator'''
import unittest
from translator import english_to_french, english_to_german

class TestEnglishToFrench(unittest.TestCase):
    '''Tests for the english_to_french function'''
    def test_translation_pos(self):
        '''Test case for positive statement'''
        self.assertEqual(english_to_french(),'Bonjour'
                        ) # English 'Hello' is 'Bonjour' in French.
    def test_translation_neg(self):
        '''Test case for negative statement'''
        self.assertNotEqual(english_to_french(),
                            'Au revoir') # English 'Hello' is not 'Au revoir' in French.

class TestEnglishToGerman(unittest.TestCase):
    '''Tests for the english_to_german function'''
    def test_translation_pos(self):
        '''Test case for positive statement'''
        self.assertEqual(english_to_german(),'Hallo'
                        ) # English 'Hello' is 'Hallo' in German.
    def test_translation_neg(self):
        '''Test case for negative statement'''
        self.assertNotEqual(english_to_german(),
                            'Auf Wiedersehen') # English 'Hello' is not 'Auf Wiedersehen' in German.


if __name__ == '__main__':
    unittest.main()
