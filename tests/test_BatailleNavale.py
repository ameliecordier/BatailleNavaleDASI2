import unittest
import utils.flotte as flotte

class TestBatailleNavale(unittest.TestCase):

    def test_Configure(self):
        monBeauBateau = flotte.Bateau()
        monBeauBateau.configure("porte-avion")
        self.assertEqual(monBeauBateau.size, 5)

#TEST
