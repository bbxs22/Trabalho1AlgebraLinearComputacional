from gaussSeidel import *
from matrix import *
from vector import *
import unittest

class TestGaussSeidel(unittest.TestCase):
    
    def test_execute_2per2_system(self):
        A = Matrix([2, 1, 1, -1], 2, 2)
        b = Vector([3, 0])
        v0 = Vector([0, 0])
        
        x = GaussSeidel.execute(A, b, v0, max_depth=100)
        
        self.assertAlmostEqual(x.get(0), 1.0, delta=0.000001)
        self.assertAlmostEqual(x.get(1), 1.0, delta=0.000001)
        
    def test_execute_3per3_system(self):
        A = Matrix([1, 1, -1, 5, 2, 1, 2, -4, 7], 3, 3)
        b = Vector([1, 8, 5])
        v0 = Vector([0, 0, 0])
        
        x = GaussSeidel.execute(A, b, v0, max_depth=100)
        
        self.assertAlmostEqual(x.get(0), 1.0, delta=0.000001)
        self.assertAlmostEqual(x.get(1), 1.0, delta=0.000001)
        self.assertAlmostEqual(x.get(2), 1.0, delta=0.000001)

if __name__ == '__main__':
    unittest.main()