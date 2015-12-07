import unittest
import utils.flotte as flotte
import Arsenal

class TestBateau(unittest.TestCase):
    def test_constructionBateau(self):
        arsenal = Arsenal.Arsenal()
        bateau = flotte.Bateau(arsenal, "porte-avion")
        self.assertEqual(bateau.taille,5)
    def test_ajoutBateau(self):
        arsenal = Arsenal.Arsenal()
        bateau = flotte.Bateau(arsenal, "torpilleur")
        self.assertEqual(bateau, arsenal.bateaux[0])


#TEST
