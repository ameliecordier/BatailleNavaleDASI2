import unittest
import utils.flotte as flotte

class TestBatailleNavale(unittest.TestCase):

    def test_Configure(self):
        monBeauBateau = flotte.Bateau()
        monBeauBateau.configure("porte-avion")
        self.assertEqual(monBeauBateau.size, 5)

<<<<<<< HEAD
    def test_monTest(self):
        self.assertEqual(2+2,5)

    def test_Erreur(self):
        print toto
=======
>>>>>>> origin/master

#unittest.main()
