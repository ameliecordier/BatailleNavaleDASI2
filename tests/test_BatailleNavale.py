import unittest
import utils.flotte as flotte

class TestBateau(unittest.TestCase):

    def test_Configure(self):
        monBeauBateau = flotte.Bateau()
        monBeauBateau.configure("porte-avion")
        self.assertEqual(monBeauBateau.size, 5)

    def test_monTest(self):
        self.assertEqual(2+2,5)

    def test_Erreur(self):
        print toto


#unittest.main()
