import unittest
from translator import englishToFrench, frenchToEnglish


class TestEngToFren(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(englishToFrench('I love you'), 'I love you')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')


class TestFrenToEng(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(frenchToEnglish('Je t''aime'), '')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()