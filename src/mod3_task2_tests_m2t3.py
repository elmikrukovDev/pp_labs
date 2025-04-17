import unittest
from mod2.task3 import decrypt

class TestDecrypt(unittest.TestCase):

    def test_single_dot(self):
        with self.subTest("абра-кадабра."):
            self.assertEqual(decrypt('абра-кадабра.'), 'абра-кадабра')

    def test_double_dots(self):
        with self.subTest("абраа..-кадабра"):
            self.assertEqual(decrypt('абраа..-кадабра'), 'абра-кадабра')
        with self.subTest("абраа..-.кадабра"):
            self.assertEqual(decrypt('абраа..-.кадабра'), 'абра-кадабра')
        with self.subTest("абра--..кадабра"):
            self.assertEqual(decrypt('абра--..кадабра'), 'абра-кадабра')
        with self.subTest("абрау...-кадабра"):
            self.assertEqual(decrypt('абрау...-кадабра'), 'абра-кадабра')

    def test_multiple_dots(self):
        with self.subTest("абра........"):
            self.assertEqual(decrypt('абра........'), '')
        with self.subTest("абр......a."):
            self.assertEqual(decrypt('абр......a.'), 'a')

    def test_numbers_and_empty(self):
        with self.subTest("1..2.3"):
            self.assertEqual(decrypt('1..2.3'), '23')
        with self.subTest("."):
            self.assertEqual(decrypt('.'), '')
        with self.subTest("1......................."):
            self.assertEqual(decrypt('1.......................'), '')

    def test_edge_cases(self):
        self.assertEqual(decrypt(""), "")
        self.assertEqual(decrypt("-"), "-")
        self.assertEqual(decrypt(".."), "")
        self.assertEqual(decrypt("..."), "")
        self.assertEqual(decrypt("a...b"), "b")

if __name__ == "__main__":
    unittest.main()