import unittest
from SimSensor.simsensor import * # From in the SimSensor folder and the simsensor python file import all the functions within
from random import Random

# This can probably be improved by understanding and implimenting the python random seed

# Black box testing that the numgen class outputs correctly
class test_numgen(unittest.TestCase):
    def test_HighLimit(self): # Test that it never outputs above 40 celsius
        for x in range(100): # Test it a 100 times (for randomness)
            self.assertLess(simsensor.numgen(), 41, 'Error: A numer output over 40')
        
    def test_LowLimit(self): # Test that it never outputs below -30 celsius
        for x in range(100): # Test it a 100 times (for randomness)
            self.assertGreater(simsensor.numgen(), -30, 'Error: A numer output below -30')
        
    def test_RandomNumber(self): # Test that the output is not *always* the same
        oldOutput = simsensor.numgen()
        maxRepeats = 3 # Numer of time the numgen function can be called and the output be allowed to repeat
        for x in range(100): # Test it a 100 times (for randomness)
            if maxRepeats <= 0:
                self.assertTrue(False, 'Error: Random output did not change') # ...in previous loop
            currentOutput = simsensor.numgen() # Get a new output to compare to
            if currentOutput == oldOutput:
                maxRepeats -= 1 # Decrease by one if random number hasen't changed
            else:
                maxRepeats = 3 # Reset maxRepeats if a new number is generated
                oldOutput = currentOutput # Make the old output the value of the current output and repeat
        self.assertTrue(True) # If it makes it though the loop its probably fine
                