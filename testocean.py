import ocean
import unittest

class TestOcean(unittest.TestCase):

    def test_constructionOcean(self):
        monOcean = []
        monOcean = construireOcean(3,7)
        self.assertEqual(monOcean.largeurOcean(),7)
        self.assertEqual(monOcean.hauteurOcean(),3)

  
unittest.main()
