import unittest
from main import *



class MyTestCase(unittest.TestCase):
    def testing(self):
        self.assertEqual(test_main(), 0.99)

if __name__ == '__main__':
    unittest.main()
