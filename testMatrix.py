from matrix import *
import unittest

class TestMatrix(unittest.TestCase):
    
    def test_get(self):
        matrix = Matrix([4, 3, 2, 2, 1, 0, 9, 7, 2, -1], 2, 5)
        self.assertAlmostEqual(matrix.get(0, 0), 4.0, delta=0.000001)
        self.assertAlmostEqual(matrix.get(1, 1), 9.0, delta=0.000001)
        self.assertAlmostEqual(matrix.get(0, 4), 1.0, delta=0.000001)
        
    def test_set(self):
        matrix = Matrix([4, 3, 2, 2, 1, 0, 9, 7, 2, -1], 2, 5)
        matrix.set(0, 0, -4)
        self.assertAlmostEqual(matrix.get(0, 0), -4.0, delta=0.000001)
        matrix.set(1, 1, -9)
        self.assertAlmostEqual(matrix.get(1, 1), -9.0, delta=0.000001)
        matrix.set(0, 4, -1)
        self.assertAlmostEqual(matrix.get(0, 4), -1.0, delta=0.000001)
        
    def test_zeros(self):
        matrix = Matrix.zeros(2, 3)
        self.assertEqual(matrix.rows(), 2)
        self.assertEqual(matrix.columns(), 3)
        
        for i in xrange(matrix.rows()):
            for j in xrange(matrix.columns()):
                self.assertAlmostEqual(matrix.get(i, j), 0.0, delta=0.000001)
                
    def test_ones(self):
        matrix = Matrix.ones(3, 2)
        self.assertEqual(matrix.rows(), 3)
        self.assertEqual(matrix.columns(), 2)
        
        for i in xrange(matrix.rows()):
            for j in xrange(matrix.columns()):
                self.assertAlmostEqual(matrix.get(i, j), 1.0, delta=0.000001)
                
    def test_eye_same_rows_columns(self):
        matrix = Matrix.eye(3, 3)
        self.assertEqual(matrix.rows(), 3)
        self.assertEqual(matrix.columns(), 3)
        
        for i in xrange(matrix.rows()):
            for j in xrange(matrix.columns()):
                if i == j:
                    self.assertAlmostEqual(matrix.get(i, j), 1.0, delta=0.000001)
                else:
                    self.assertAlmostEqual(matrix.get(i, j), 0.0, delta=0.000001)
                    
    def test_eye_rows_greater_than_columns(self):
        matrix = Matrix.eye(3, 5)
        self.assertEqual(matrix.rows(), 3)
        self.assertEqual(matrix.columns(), 5)
        
        for i in xrange(matrix.rows()):
            for j in xrange(matrix.columns()):
                if i == j:
                    self.assertAlmostEqual(matrix.get(i, j), 1.0, delta=0.000001)
                else:
                    self.assertAlmostEqual(matrix.get(i, j), 0.0, delta=0.000001)
                    
    def test_eye_columns_greater_than_rows(self):
        matrix = Matrix.eye(5, 3)
        self.assertEqual(matrix.rows(), 5)
        self.assertEqual(matrix.columns(), 3)
        
        for i in xrange(matrix.rows()):
            for j in xrange(matrix.columns()):
                if i == j:
                    self.assertAlmostEqual(matrix.get(i, j), 1.0, delta=0.000001)
                else:
                    self.assertAlmostEqual(matrix.get(i, j), 0.0, delta=0.000001)
                    
    def test_copy(self):
        matrix = Matrix.ones(2, 2)
        matrix2 = matrix.copy()
        matrix2.set(0, 0, 12.0)
        self.assertAlmostEqual(matrix.get(0, 0), 1.0, delta=0.000001)
        self.assertAlmostEqual(matrix2.get(0, 0), 12.0, delta=0.000001)
        
    def test_transpose(self):
        matrix = Matrix([1, 2, 3, 4], 2, 2)
        matrix2 = matrix.transpose()
        self.assertAlmostEqual(matrix.get(0, 0), 1.0, delta=0.000001)
        self.assertAlmostEqual(matrix.get(0, 1), 2.0, delta=0.000001)
        self.assertAlmostEqual(matrix.get(1, 0), 3.0, delta=0.000001)
        self.assertAlmostEqual(matrix.get(1, 1), 4.0, delta=0.000001)
        self.assertAlmostEqual(matrix2.get(0, 0), 1.0, delta=0.000001)
        self.assertAlmostEqual(matrix2.get(0, 1), 3.0, delta=0.000001)
        self.assertAlmostEqual(matrix2.get(1, 0), 2.0, delta=0.000001)
        self.assertAlmostEqual(matrix2.get(1, 1), 4.0, delta=0.000001)
        
    def test_norm(self):
        vector = Matrix([4, 3, 2, 5], 2, 2)
        self.assertAlmostEqual(vector.norm(), math.sqrt(4**2+3**2+2**2+5**2), delta=0.000001)

    def test_sub(self):
        matrix = Matrix([4, 3, 2, 2, 1, 0, 9, 7, 2, -1], 2, 5)
        matrix2 = Matrix.ones(2, 5)
        result = matrix - matrix2
        
        self.assertAlmostEqual(result.get(0, 0), 3.0, delta=0.000001)
        self.assertAlmostEqual(result.get(0, 1), 2.0, delta=0.000001)
        self.assertAlmostEqual(result.get(0, 2), 1.0, delta=0.000001)
        self.assertAlmostEqual(result.get(0, 3), 1.0, delta=0.000001)
        self.assertAlmostEqual(result.get(0, 4), 0.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 0), -1.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 1), 8.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 2), 6.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 3), 1.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 4), -2.0, delta=0.000001)
        
    def test_mul_between_matrices(self):
        matrix = Matrix([3, 8, 1, -1], 2, 2)
        matrix2 = Matrix([1, 2, 3, 3], 2, 2)
        result = matrix * matrix2
        
        self.assertAlmostEqual(result.get(0, 0), 27.0, delta=0.000001)
        self.assertAlmostEqual(result.get(0, 1), 30.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 0), -2.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 1), -1.0, delta=0.000001)

        
    def test_mul_between_matrix_constant(self):
        matrix = Matrix([3, 8, 1, -1], 2, 2)
        
        result = matrix * 2
        self.assertAlmostEqual(result.get(0, 0), 6.0, delta=0.000001)
        self.assertAlmostEqual(result.get(0, 1), 16.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 0), 2.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 1), -2.0, delta=0.000001)
        
        result = 3 * matrix
        self.assertAlmostEqual(result.get(0, 0), 9.0, delta=0.000001)
        self.assertAlmostEqual(result.get(0, 1), 24.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 0), 3.0, delta=0.000001)
        self.assertAlmostEqual(result.get(1, 1), -3.0, delta=0.000001)
        
    def test_get_row(self):
        matrix = Matrix([3, 8, 1, -1], 2, 2)
        row_vector = matrix.get_row(1)
        self.assertEqual(row_vector.rows(), 1)
        self.assertEqual(row_vector.columns(), 2)
        self.assertAlmostEqual(row_vector.get(0), 1.0, delta=0.000001)
        self.assertAlmostEqual(row_vector.get(1), -1.0, delta=0.000001)

    def test_tolist(self):
        matrix = Matrix([3, 8, 1, -1], 2, 2)
        array = matrix.tolist()
        self.assertEqual(len(array), 2)
        self.assertEqual(len(array[0]), 2)
        self.assertAlmostEqual(array[0][0], 3.0, delta=0.000001)
        self.assertAlmostEqual(array[0][1], 8.0, delta=0.000001)
        self.assertEqual(len(array[1]), 2)
        self.assertAlmostEqual(array[1][0], 1.0, delta=0.000001)
        self.assertAlmostEqual(array[1][1], -1.0, delta=0.000001)
        
        matrix2 = Matrix([3, 8, 1, -1, 4, 5], 3, 2)
        array = matrix2.tolist()
        self.assertEqual(len(array), 3)
        self.assertEqual(len(array[0]), 2)
        self.assertAlmostEqual(array[0][0], 3.0, delta=0.000001)
        self.assertAlmostEqual(array[0][1], 8.0, delta=0.000001)
        self.assertEqual(len(array[1]), 2)
        self.assertAlmostEqual(array[1][0], 1.0, delta=0.000001)
        self.assertAlmostEqual(array[1][1], -1.0, delta=0.000001)
        self.assertEqual(len(array[2]), 2)
        self.assertAlmostEqual(array[2][0], 4.0, delta=0.000001)
        self.assertAlmostEqual(array[2][1], 5.0, delta=0.000001)
        

if __name__ == '__main__':
    unittest.main()