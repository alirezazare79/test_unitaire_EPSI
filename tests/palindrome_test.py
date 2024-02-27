import os
import unittest

from tests.utilities.palindrome_builder import PalindromeBuilder

cas_palindrome_valide = ["kayak", "radar", "s.o.s", "été"]
cas_palindrome_invalide = ["bonjour", "hello", "au revoir", "bien dit"]
cas_palindrome_valide_invalide = cas_palindrome_valide + cas_palindrome_invalide

class TestPalindrome(unittest.TestCase):
    def test_mirroir(self):
        for cas in cas_palindrome_valide_invalide:
            with self.subTest(cas):
                self.assertEqual(PalindromeBuilder().build().mirroir(cas), cas[::-1])

    def test_palindrome(self):
        for cas in cas_palindrome_valide:
            attendu = cas + os.linesep + "bien dit"
            with self.subTest(cas):
                self.assertEqual(PalindromeBuilder().build().palindrome(cas), attendu)

    def test_palindrome_invalide(self):
        for cas in cas_palindrome_invalide:
            with self.subTest(cas):
                self.assertEqual(PalindromeBuilder().build().palindrome(cas), cas)