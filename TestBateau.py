import unittest
import Bateau
import Arsenal



class TestBateau(unittest.TestCase):
    def test_constructionBateau(self):
        arsenal = Arsenal.Arsenal()
        bateau = Bateau.Bateau(arsenal, "PorteAvion")
        self.assertEqual(bateau.taille,5)
    def test_ajoutBateau(self):
        arsenal = Arsenal.Arsenal()
        bateau = Bateau.Bateau(arsenal, "Radeau")
        self.assertEqual(bateau, arsenal.bateaux[0])
    


unittest.main()


