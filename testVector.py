from vector import *
import unittest

class TestVector(unittest.TestCase):

    def test_new_vector(self):
        vector = Vector([4, 3, 2])
        self.assertEqual(vector.rows(), 3)
        self.assertEqual(vector.columns(), 1)
        
        vector2 = Vector([-4, -3, -2], False)
        self.assertEqual(vector2.rows(), 1)
        self.assertEqual(vector2.columns(), 3)
    
    def test_get(self):
        vector = Vector([4, 3, 2])
        self.assertAlmostEqual(vector.get(0), 4.0, delta=0.000001)
        self.assertAlmostEqual(vector.get(1), 3.0, delta=0.000001)
        self.assertAlmostEqual(vector.get(2), 2.0, delta=0.000001)
        
        vector2 = Vector([-4, -3, -2], False)
        self.assertAlmostEqual(vector2.get(0), -4.0, delta=0.000001)
        self.assertAlmostEqual(vector2.get(1), -3.0, delta=0.000001)
        self.assertAlmostEqual(vector2.get(2), -2.0, delta=0.000001)
        
    def test_set(self):
        vector = Vector([4, 3, 2])
        vector.set(0, -2)
        self.assertAlmostEqual(vector.get(0), -2.0, delta=0.000001)
        vector.set(1, -3)
        self.assertAlmostEqual(vector.get(1), -3.0, delta=0.000001)
        vector.set(2, -4)
        self.assertAlmostEqual(vector.get(2), -4.0, delta=0.000001)
        
        vector2 = Vector([-4, -3, -2], False)
        vector2.set(0, 4)
        self.assertAlmostEqual(vector2.get(0), 4.0, delta=0.000001)
        vector2.set(1, 3)
        self.assertAlmostEqual(vector2.get(1), 3.0, delta=0.000001)
        vector2.set(2, 2)
        self.assertAlmostEqual(vector2.get(2), 2.0, delta=0.000001)
        
    def test_copy(self):
        vector = Vector([4, 3, 2])
        self.assertEqual(vector.rows(), 3)
        self.assertEqual(vector.columns(), 1)
        
        vector2 = vector.copy()
        self.assertEqual(vector.rows(), 3)
        self.assertEqual(vector.columns(), 1)
        
        vector2.set(2, 10)
        self.assertAlmostEqual(vector.get(2), 2.0, delta=0.000001)
        self.assertAlmostEqual(vector2.get(2), 10.0, delta=0.000001)
        
    def test_transpose(self):
        vector = Vector([4, 3, 2])
        self.assertEqual(vector.rows(), 3)
        self.assertEqual(vector.columns(), 1)
        
        vector2 = vector.transpose()
        self.assertEqual(vector.rows(), 3)
        self.assertEqual(vector.columns(), 1)
        self.assertEqual(vector2.rows(), 1)
        self.assertEqual(vector2.columns(), 3)
        
        vector2.set(2, 10)
        self.assertAlmostEqual(vector.get(2), 2.0, delta=0.000001)
        self.assertAlmostEqual(vector2.get(2), 10.0, delta=0.000001)
        
    def test_norm(self):
        vector = Vector([4, 3, 2])
        self.assertAlmostEqual(vector.norm(), math.sqrt(4**2+3**2+2**2), delta=0.000001)
        
    def test_dot_product(self):
        vector = Vector([4, 3, 2], False)
        vector2 = Vector([4, 3, 2])
        self.assertAlmostEqual(vector.dot_product(vector2), 29.0, delta=0.000001)
        
    def test_add(self):
        vector1 = Vector([4, 1, 2], False)
        vector2 = Vector([2, 3, -1], False)
        vector3 = vector1 + vector2
        
        self.assertAlmostEqual(vector3.get(0), 6.0, delta=0.000001)
        self.assertAlmostEqual(vector3.get(1), 4.0, delta=0.000001)
        self.assertAlmostEqual(vector3.get(2), 1.0, delta=0.000001)
        
    def test_sub(self):
        vector1 = Vector([4, 3, 2])
        vector2 = Vector([2, 3, 4])
        vector3 = vector1 - vector2
        
        self.assertAlmostEqual(vector3.get(0), 2.0, delta=0.000001)
        self.assertAlmostEqual(vector3.get(1), 0.0, delta=0.000001)
        self.assertAlmostEqual(vector3.get(2), -2.0, delta=0.000001)
        
    def test_mul_between_vectors(self):
        vector = Vector([1, 2, 3])
        vector2 = Vector([4, 5, 6], False)
        matrix = vector * vector2
        self.assertAlmostEqual(matrix.get(0, 0), 4.0, delta=0.000001)
        self.assertAlmostEqual(matrix.get(0, 1), 5.0, delta=0.000001)
        self.assertAlmostEqual(matrix.get(0, 2), 6.0, delta=0.000001)
        self.assertAlmostEqual(matrix.get(1, 0), 8.0, delta=0.000001)
        self.assertAlmostEqual(matrix.get(1, 1), 10.0, delta=0.000001)
        self.assertAlmostEqual(matrix.get(1, 2), 12.0, delta=0.000001)
        self.assertAlmostEqual(matrix.get(2, 0), 12.0, delta=0.000001)
        self.assertAlmostEqual(matrix.get(2, 1), 15.0, delta=0.000001)
        self.assertAlmostEqual(matrix.get(2, 2), 18.0, delta=0.000001)
        
        vector = Vector([4, 3, 2], False)
        vector2 = Vector([4, 3, 2])
        self.assertAlmostEqual(vector.dot_product(vector2), 29.0, delta=0.000001)
        
    def test_mul_between_vector_constant(self):
        vector = Vector([1, 2, 3])
        result = vector * 2
        self.assertEqual(result.rows(), 3)
        self.assertEqual(result.columns(), 1)
        self.assertAlmostEqual(result.get(0), 2.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1), 4.0, delta=0.000001)
        self.assertAlmostEqual(result.get(2), 6.0, delta=0.000001)
        
        result = 2 * vector
        self.assertEqual(result.rows(), 3)
        self.assertEqual(result.columns(), 1)
        self.assertAlmostEqual(result.get(0), 2.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1), 4.0, delta=0.000001)
        self.assertAlmostEqual(result.get(2), 6.0, delta=0.000001)


if __name__ == '__main__':
    unittest.main()