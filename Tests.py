import unittest
import ocean

class TestBatailleMethods(unittest.TestCase):

    def test_constructionOcean(self):
        monOcean = creerOcean (3,7)
        self.assertEqual(len(monOcean),7)
        self.assertEqual(len(monOcean[0]),3)
    
unittest.main()
