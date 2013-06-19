from lsi import *
import math
import unittest

class TestLSI(unittest.TestCase):

    def test_calculate_svd(self):
        u, s, v = LSI.calculate_svd(Matrix([1, -1, 1, -1, math.sqrt(3), 0], 3, 2))
        
        self.assertEqual(u.rows(), 3)
        self.assertEqual(u.columns(), 2)
        self.assertEqual(s.rows(), 2)
        self.assertEqual(s.columns(), 1)
        self.assertAlmostEqual(s.get(0), 2.4494897, delta=0.000001)
        self.assertAlmostEqual(s.get(1), 1.0, delta=0.000001)
        self.assertEqual(v.rows(), 2)
        self.assertEqual(v.columns(), 2)
        self.assertAlmostEqual(v.get(0, 0), -0.8944271, delta=0.000001)
        self.assertAlmostEqual(v.get(0, 1), 0.4472135, delta=0.000001)
        self.assertAlmostEqual(v.get(1, 0), 0.4472135, delta=0.000001)
        self.assertAlmostEqual(v.get(1, 1), 0.8944271, delta=0.000001)

if __name__ == '__main__':
    unittest.main()