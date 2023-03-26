import unittest
import lib.TestCode

class testing1(unittest.TestCase):
    def testAddition(self):
        self.assertEqual(lib.TestCode.addTogether(3,4),7)
        
    def testFails(self):
        self.assertNotEqual(lib.TestCode.addTogether(4,4),7)

