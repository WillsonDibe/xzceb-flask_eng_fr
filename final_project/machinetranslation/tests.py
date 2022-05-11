import unittest
from translator import english_to_french, french_to_english
class TestEnglishtoFrench (unittest.TestCase):
    def test_1_Eng_Fre(self):
        self.assertEqual(english_to_french(' '),' ')
        self.assertEqual(english_to_french('Hello'),'Bonjour')
class TestFrenchtoEnglish(unittest.TestCase):
    def test_2_Fre_Eng(self):
        self.assertEqual(french_to_english(' '),' ')
        self.assertEqual(french_to_english('Bonjour'),'Hello')  
unittest.main()