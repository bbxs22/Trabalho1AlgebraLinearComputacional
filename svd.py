import math
from qr import *
from matrix import *

class SVD:

    @staticmethod
    def calculate_eigenvalues_eigenvectors(matrix, error=0.000001):
        '''
        Calcula autovalores de uma matriz quadrada simetrica
        @param float (optional)
        @param Matrix
        @return tuple<int,list,Matrix>
        '''
        iterations = 0
        previous_value, current_value = 1, 0
        eigenvectors = matrix.eye(matrix.rows(), matrix.rows())
        while abs(current_value - previous_value) > error:
            Q, R = QR.execute(matrix)
            matrix = R * Q
            eigenvectors = eigenvectors * Q
            iterations = iterations + 1
            previous_value, current_value = current_value, matrix.get(1, 0)

        eigenvalues = list()
        for j in xrange(matrix.columns()):
            eigenvalues.append(matrix.get(j, j))
            
        return iterations, eigenvalues, eigenvectors