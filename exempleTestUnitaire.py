import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_qui_fail(self):
        self.assertEqual('bar'.upper(), 'BAR')
  
unittest.main()
