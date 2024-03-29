import unittest
from equation import Klass 

class TestEquation(unittest.TestCase):

    def setUp(self):
        self.Klass = Klass()

    def test_PositiveDiscriminant(self):
        self.assertEqual(self.Klass.discriminant(3, 7, -6), 121)
    
    def test_ZeroDiscriminant(self):
        self.assertEqual(self.Klass.discriminant(4, 4, 1), 0)

    def test_NegativeDiscriminant(self):
        self.assertEqual(self.Klass.discriminant(2, 1, 1), -7)
        
    def test_Squareroot(self):
        self.assertEqual(self.Klass.squareroot(1, 0), 0.0)
        
    def test_Squareroots(self):
        self.assertEqual(self.Klass.squareroots(1, 2, 16), [-3.0, 1])
  
if __name__ == "__main__":
    unittest.main()