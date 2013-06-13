from svd import *
import unittest

class TestSVD(unittest.TestCase):

    def test_new_svd(self):
        SVD.MATLAB_U = 'test/svd/u.txt'
        SVD.MATLAB_S = 'test/svd/s.txt'
        SVD.MATLAB_V = 'test/svd/v.txt'

        svd = SVD()
        self.assertAlmostEqual(svd.score_vector.get(0), 3.0024077, delta=0.000001)
        self.assertAlmostEqual(svd.score_vector.get(1), 2.9208098, delta=0.000001)

    def test_read_matrix(self):
        matrix = SVD.read_matrix('test/svd/test_read_matrix.txt')
        self.assertEqual(matrix.rows(), 2)
        self.assertEqual(matrix.columns(), 2)
        self.assertAlmostEqual(matrix.get(0, 0), 3.002407, delta=0.000001)
        self.assertAlmostEqual(matrix.get(0, 1), 0.0, delta=0.000001)
        self.assertAlmostEqual(matrix.get(1, 0), 0.0, delta=0.000001)
        self.assertAlmostEqual(matrix.get(1, 1), 2.920809, delta=0.000001)
        
    def test_get_query_vector(self):
        SVD.MATLAB_U = 'test/svd/u.txt'
        SVD.MATLAB_S = 'test/svd/s.txt'
        SVD.MATLAB_V = 'test/svd/v.txt'

        svd = SVD()
        vector = svd.get_query_vector([3, 4])
        self.assertAlmostEqual(vector.get(0), -0.3847023, delta=0.000001)
        self.assertAlmostEqual(vector.get(1), -0.2466640, delta=0.000001)
        
    def get_row_vectors(self):
        SVD.MATLAB_U = 'test/svd/u.txt'
        SVD.MATLAB_S = 'test/svd/s.txt'
        SVD.MATLAB_V = 'test/svd/v.txt'

        svd = SVD()
        doc_vectors = svd.get_row_vectors(svd.v)
        self.assertEqual(len(doc_vectors), 9)
        self.assertAlmostEqual(doc_vectors[0].get(0), -0.4595774, delta=0.000001)
        self.assertAlmostEqual(doc_vectors[0].get(1), -0.3474577, delta=0.000001)
        self.assertAlmostEqual(doc_vectors[1].get(0), -0.5578699, delta=0.000001)
        self.assertAlmostEqual(doc_vectors[1].get(1), -0.2612275, delta=0.000001)
        self.assertAlmostEqual(doc_vectors[2].get(0), -0.2303408, delta=0.000001)
        self.assertAlmostEqual(doc_vectors[2].get(1), -0.1590020, delta=0.000001)

if __name__ == '__main__':
    unittest.main()