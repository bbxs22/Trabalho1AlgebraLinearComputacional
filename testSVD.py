from svd import *
from qr import *
from householder import *
import unittest

class TestSVD(unittest.TestCase):

    def test_calculate_eigenvalues_eigenvectors(self):
        A = Matrix([52, 30, 49, 28, 30, 50, 8, 44, 49, 8, 46, 16, 28, 44, 16, 22], 4, 4)
        #AT = A.transpose()
        #AAT = A * AT
        
        # transforma matriz simetrica em uma tridiagonal
        AAT = Householder.execute(AAT)
        
        # encontra os autovalores via QR
        iterations, eigenvalues, eigenvectors = SVD.calculate_eigenvalues_eigenvectors(AAT)
        
        self.assertAlmostEqual(eigenvalues[0], 132.6279, delta=0.000001)
        self.assertAlmostEqual(eigenvalues[1], 52.4423, delta=0.000001)
        self.assertAlmostEqual(eigenvalues[2], -11.54113, delta=0.000001)
        self.assertAlmostEqual(eigenvalues[3], -3.52904, delta=0.000001)
        
#        self.assertAlmostEqual(eigenvectors.get(0, 0), 1.0, delta=0.000001)
#        self.assertAlmostEqual(eigenvectors.get(0, 1), 1.0, delta=0.000001)
#        self.assertAlmostEqual(eigenvectors.get(1, 0), 1.0, delta=0.000001)
#        self.assertAlmostEqual(eigenvectors.get(1, 1), -1.0, delta=0.000001)
    
    def test_calculate_eigenvalues_eigenvectors_rectangular_matrix(self):
        A = Matrix([3, 1, 1, -1, 3, 1], 2, 3)
        AT = A.transpose()
        AAT = A * AT
        
        self.assertAlmostEqual(AAT.get(0, 0), 11.0, delta=0.000001)
        self.assertAlmostEqual(AAT.get(0, 1), 1.0, delta=0.000001)
        self.assertAlmostEqual(AAT.get(1, 0), 1.0, delta=0.000001)
        self.assertAlmostEqual(AAT.get(1, 1), 11.0, delta=0.000001)
        
        # transforma matriz simetrica em uma tridiagonal
        AAT = Householder.execute(AAT)
        
        # encontra os autovalores via QR
        iterations, eigenvalues, eigenvectors = SVD.calculate_eigenvalues_eigenvectors(AAT)

        self.assertAlmostEqual(AAT.get(0, 0), 11.0, delta=0.000001)
        self.assertAlmostEqual(AAT.get(0, 1), 1.0, delta=0.000001)
        self.assertAlmostEqual(AAT.get(1, 0), 1.0, delta=0.000001)
        self.assertAlmostEqual(AAT.get(1, 1), 11.0, delta=0.000001)
        
        self.assertAlmostEqual(eigenvalues[0], 12.0, delta=0.000001)
        self.assertAlmostEqual(eigenvalues[1], 10.0, delta=0.000001)
        
        self.assertAlmostEqual(eigenvectors.get(0, 0), 1.0, delta=0.000001)
        self.assertAlmostEqual(eigenvectors.get(0, 1), 1.0, delta=0.000001)
        self.assertAlmostEqual(eigenvectors.get(1, 0), 1.0, delta=0.000001)
        self.assertAlmostEqual(eigenvectors.get(1, 1), -1.0, delta=0.000001)

    def test_calculate_eigenvalues_eigenvectors_square_matrix(self):
        A = Matrix([2, 0, 8, 6, 0, 1, 6, 0, 1, 7, 5, 0, 7, 4, 0, 7, 0, 8, 5, 0, 0, 10, 0, 0, 7], 5, 5)
        AT = A.transpose()
        AAT = A * AT
        
        # transforma matriz simetrica em uma tridiagonal
        AAT = Householder.execute(AAT)
        
        # encontra os autovalores via QR
        iterations, eigenvalues, eigenvectors = SVD.calculate_eigenvalues_eigenvectors(AAT)
            
        self.assertAlmostEqual(eigenvalues[0], 321.07, delta=0.1)
        self.assertAlmostEqual(eigenvalues[1], 230.17, delta=0.1)
        self.assertAlmostEqual(eigenvalues[2], 12.70, delta=0.1)
        self.assertAlmostEqual(eigenvalues[3], 3.94, delta=0.1)
        self.assertAlmostEqual(eigenvalues[4], 0.12, delta=0.1)

if __name__ == '__main__':
    unittest.main()