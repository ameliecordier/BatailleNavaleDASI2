import unittest
import utils.flotte as flotte
import Arsenal

class TestBateau(unittest.TestCase):
    def test_constructionBateau(self):
        bateau = flotte.Bateau()
        bateau.configure("porte-avion")
        self.assertEqual(bateau.size,5)
    def test_ajoutBateau(self):
        arsenal = Arsenal.Arsenal()
        bateau = flotte.Bateau()
        bateau.configure("torpilleur")
        arsenal.ajouterBateau(bateau)
        self.assertEqual(bateau, arsenal.bateaux[0])


#TEST