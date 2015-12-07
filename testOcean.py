# -*- coding: utf8 -*-

import unittest ##pour les tests
import classeOcean

class TestOcean(unittest.TestCase):
    def test_construitOcean_bonneTaille(self):
        o = classeOcean.ocean(3, 7)
        self.assertEqual(len(o.grille), 3)
        self.assertEqual(len(o.grille[0]), 7)

        
    def test_construitOcean_longueurIdentique(self):
        o = classeOcean.ocean(3, 7)
        
        for i in range(0, 3):
            self.assertEqual(len(o.grille[i]), 7)

        
    def test_construitOcean_contenuListe(self):
        o = classeOcean.ocean(3, 7)
        
        for y in range(-1, 7):
            for x in range(-1, 3):
                self.assertEqual(o.grille[x][y], "o")



print("\nDébut des tests d'ocean.")
unittest.main()
