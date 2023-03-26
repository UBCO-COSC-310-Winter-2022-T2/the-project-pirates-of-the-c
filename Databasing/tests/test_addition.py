import unittest
from lib.TestCode import *

class testing1(unittest.TestCase):
    def testAddition(self):
        self.assertEqual(addTogether(3,4),7)
        
    def testFails(self):
        self.assertNotEqual(addTogether(4,4),7)

