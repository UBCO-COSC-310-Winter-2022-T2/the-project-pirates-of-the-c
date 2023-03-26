import unittest # Import the unittest framework
from simsensor import * # Import the numgen python file from lib folder and all functions within
from random import Random

# This can probably be improved by figuring out and implimenting the python random seed

# Black box testing that the numgen class outputs correctly
class testsensor(unittest.TestCase):
    def testHigh(self): # Test that it never outputs above 40
        for x in range(100): # Test it a 100 times (for randomness)
            self.assertLess(numgen(), 41, 'Error: A numer output over 40')
        
    def testLow(self): # Test that it never outputs below -30
        for x in range(100): # Test it a 100 times (for randomness)
            self.assertGreater(numgen(), -30, 'Error: A numer output below -30')
        
    def testRandom(self): # Test that the output is not *always* the same
        newOutput = numgen()
        maxRepeats = 3
        for x in range(100): # Test it a 100 times (for randomness)
            currentOutput = numgen()
            if currentOutput == newOutput:
                maxRepeats -= 1 # Decrease by one if random number hasen't changed
            else:
                maxRepeats = 3 # Reset maxRepeats if a new number is generated
            
            
