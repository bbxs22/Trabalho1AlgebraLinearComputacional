import math
from matrix import *

class QR:

    @staticmethod
    def calculate_P(matrix, row, column):
        '''
        Gera a matriz de rotacao P
        @param Matrix
        @param int
        @param int
        @return Matrix
        '''
        P = Matrix.eye(matrix.rows(), matrix.rows())
        
        # calcula sin e cos
        a = matrix.get(row, column)
        b = matrix.get(row, column+1)
        cos_theta = a / math.sqrt(a * a + b * b)
        sin_theta = b / math.sqrt(a * a + b * b)
        
        # ajusta na matriz de rotacao P
        P.set(row, column, cos_theta)
        P.set(row, column+1, sin_theta)
        P.set(row+1, column, -sin_theta)
        P.set(row+1, column+1, cos_theta)
        
        return P

    @staticmethod
    def execute(matrix):
        '''
        Executa o metodo para transformar a matrix numa matriz quase triangular superior ou numa tridiagonal
        @param Matrix
        @return Matrix
        '''
        R = matrix.copy()
        Q = Matrix.eye(matrix.rows(), matrix.rows())
        
        iterations = 0
        while iterations < matrix.rows() - 1:
            # gera a matriz de rotacao
            P = QR.calculate_P(R, iterations, iterations)
            
            # multiplica P pela matriz
            R = P * R
            Q = Q * P.transpose()
            
            iterations += 1
            
        return (Q, R)