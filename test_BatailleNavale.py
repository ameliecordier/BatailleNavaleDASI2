import unittest
import flotte

class TestBateau(unittest.TestCase):

    def test_Configure(self):
        monBeauBateau = flotte.Bateau()
        monBeauBateau.configure("porte-avion")
        self.assertEqual(monBeauBateau.size, 5)

#unittest.main()
