import unittest
from src.util import generateEvents

class TestGenerateEvents(unittest.TestCase):

    def test_corrected_return_size_when_n_equals_5(self):
        self.assertEqual(5, len(generateEvents(5)))

    def test_n_equals_1(self):
        self.assertEqual(1, len(generateEvents(1)))

    def test_n_equals_0(self):
        with self.assertRaises(ValueError):
            generateEvents(0)