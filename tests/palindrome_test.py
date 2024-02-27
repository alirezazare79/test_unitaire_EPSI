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
            attendu = "bien dit"
            with self.subTest(cas):
                cas_resultat = PalindromeBuilder().build().palindrome(cas).split(os.linesep)
                self.assertEqual(cas_resultat[2], attendu)
                self.assertEqual(cas_resultat[1], cas)
                self.assertEqual(len(cas_resultat), 4)
    def test_palindrome_invalide(self):
        for cas in cas_palindrome_invalide:
            with self.subTest(cas):
                builder = PalindromeBuilder().build()
                result_split = builder.palindrome(cas).split(os.linesep)
                self.assertEqual(result_split[1], cas)
                self.assertEqual(len(result_split), 3)
    def test_palindrome_bonjour(self):
        for cas in cas_palindrome_valide_invalide:
            with self.subTest(cas):
                builder = PalindromeBuilder().build()
                result_split = builder.palindrome(cas).split(os.linesep)
                attendu = "bonjour"
                self.assertEqual(result_split[0], attendu)

    def test_palindrome_au_revoir(self):
        for cas in cas_palindrome_valide_invalide:
            with self.subTest(cas):
                builder = PalindromeBuilder().build()
                result_split = builder.palindrome(cas).split(os.linesep)
                attendu = "au revoir"
                self.assertEqual(result_split[-1], attendu)