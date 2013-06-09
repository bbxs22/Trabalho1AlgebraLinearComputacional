from qr import *
import unittest

class TestQR(unittest.TestCase):
    
    def test_calculate_P(self):
        P = QR.calculate_P(Matrix([3, 1, 0, 1, 3, 1, 0, 1, 3], 3, 3), 0, 0)
        
        self.assertAlmostEqual(P.get(0, 0), 3.0 * math.sqrt(10.0) / 10.0, delta=0.000001)
        self.assertAlmostEqual(P.get(0, 1), math.sqrt(10.0) / 10.0, delta=0.000001)
        self.assertAlmostEqual(P.get(0, 2), 0.0, delta=0.000001)
        self.assertAlmostEqual(P.get(1, 0), -math.sqrt(10.0) / 10.0, delta=0.000001)
        self.assertAlmostEqual(P.get(1, 1), 3 * math.sqrt(10.0) / 10.0, delta=0.000001)
        self.assertAlmostEqual(P.get(1, 2), 0.0, delta=0.000001)
        self.assertAlmostEqual(P.get(2, 0), 0.0, delta=0.000001)
        self.assertAlmostEqual(P.get(2, 1), 0.0, delta=0.000001)
        self.assertAlmostEqual(P.get(2, 2), 1.0, delta=0.000001)
        
    def teste_execute_square_matrix(self):
        Q, R = QR.execute(Matrix([3, 1, 0, 1, 3, 1, 0, 1, 3], 3, 3))
        result = Q * R

        self.assertAlmostEqual(result.get(0, 0), 3.0, delta=0.000001)
        self.assertAlmostEqual(result.get(0, 1), 1.0, delta=0.000001)
        self.assertAlmostEqual(result.get(0, 2), 0.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 0), 1.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 1), 3.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 2), 1.0, delta=0.000001)
        self.assertAlmostEqual(result.get(2, 0), 0.0, delta=0.000001)
        self.assertAlmostEqual(result.get(2, 1), 1.0, delta=0.000001)
        self.assertAlmostEqual(result.get(2, 2), 3.0, delta=0.000001)
        
#        self.assertAlmostEqual(Q.get(0, 0), 3.0 * math.sqrt(10.0) / 10.0, delta=0.0001)
#        self.assertAlmostEqual(Q.get(0, 1), -8.0 * math.sqrt(10.0) / (10.0 * math.sqrt(73.0)), delta=0.0001)
#        self.assertAlmostEqual(Q.get(0, 2), 3.0 * math.sqrt(10.0) / (10.0 * math.sqrt(73.0)), delta=0.0001)
#        self.assertAlmostEqual(Q.get(1, 0), math.sqrt(10.0) / 10.0, delta=0.0001)
#        self.assertAlmostEqual(Q.get(1, 1), 24.0 * math.sqrt(10.0) / (10.0 * math.sqrt(73.0)), delta=0.0001)
#        self.assertAlmostEqual(Q.get(1, 2), -9.0 * math.sqrt(10.0) / (10.0 * math.sqrt(73.0)), delta=0.0001)
#        self.assertAlmostEqual(Q.get(2, 0), 0.0, delta=0.0001)
#        self.assertAlmostEqual(Q.get(2, 1), 3.0 * math.sqrt(73.0), delta=0.0001)
#        self.assertAlmostEqual(Q.get(2, 2), 8.0 * math.sqrt(73.0), delta=0.0001)
        
#        self.assertAlmostEqual(R.get(0, 0), math.sqrt(10.0), delta=0.0001)
#        self.assertAlmostEqual(R.get(0, 1), 6 * math.sqrt(10.0) / 10.0, delta=0.0001)
#        self.assertAlmostEqual(R.get(0, 2), math.sqrt(10.0) / 10.0, delta=0.0001)
#        self.assertAlmostEqual(R.get(1, 0), 0.0, delta=0.0001)
#        self.assertAlmostEqual(R.get(1, 1), 64.0 * math.sqrt(10.0) / (10.0 * math.sqrt(73.0)) + 3.0 / math.sqrt(73.0), delta=0.0001)
#        self.assertAlmostEqual(R.get(1, 2), 24.0 * math.sqrt(10.0) / (10.0 * math.sqrt(73.0)) + 9.0 / math.sqrt(73.0), delta=0.0001)
#        self.assertAlmostEqual(R.get(2, 0), 0.0, delta=0.0001)
#        self.assertAlmostEqual(R.get(2, 1), -24.0 * math.sqrt(10.0) / (10.0 * math.sqrt(73.0)) + 8.0 / math.sqrt(73.0), delta=0.0001)
#        self.assertAlmostEqual(R.get(2, 2), -9.0 * math.sqrt(10.0) / (10.0 * math.sqrt(73.0)) + 24.0 / math.sqrt(73.0), delta=0.0001)
        
    def teste_execute_rectangle_matrix(self):
        Q, R = QR.execute(Matrix([1, 7, 3, 4, 5, 1], 3, 2))
        result = Q * R

        self.assertAlmostEqual(result.get(0, 0), 1.0, delta=0.000001)
        self.assertAlmostEqual(result.get(0, 1), 7.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 0), 3.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 1), 4.0, delta=0.000001)
        self.assertAlmostEqual(result.get(2, 0), 5.0, delta=0.000001)
        self.assertAlmostEqual(result.get(2, 1), 1.0, delta=0.000001)

if __name__ == '__main__':
    unittest.main()