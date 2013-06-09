import math
from vector import *
from matrix import *

class Householder:

    @staticmethod
    def calculate_alpha(matrix, column=0):
        '''
        Calcula valor de alpha para a coluna indicada
        @param Matrix
        @param int (optional)
        @return float
        '''
        alpha = 0.0
        for row in xrange(column + 1, matrix.rows()):
            alpha += matrix.get(row, column) ** 2
        alpha = math.sqrt(alpha)
        return alpha
        
    @staticmethod
    def calculate_w(matrix, column=0):
        '''
        Calcula o vetor w da coluna indicada da matriz
        @param Matrix
        @param int (optional)
        @return Vector
        '''
        # calcula alpha
        alpha = Householder.calculate_alpha(matrix, column)
        
        # calcula r
        r = math.sqrt((alpha ** 2) / 2.0 + (matrix.get(column+1, column) * alpha) / 2.0)
        
        # calcula w
        w = list()
        # w1
        w.append((matrix.get(column+1, column) + alpha) / (2.0 * r))
        #w2 ... wm
        for i in xrange(column+2, matrix.rows()):
            w.append(matrix.get(i, column) / (2.0 * r))
            
        return Vector(w)
    
    @staticmethod
    def calculate_P(matrix, column=0):
        '''
        Calcula a matriz P de reflexao dada por
            
            P = I - 2 / (wT * w) * (w * wT)
            
        @param Matrix
        @param int (optional)
        @return Matrix
        '''
        # matriz identidade
        P = Matrix.eye(matrix.rows(), matrix.columns())
        
        # calcula w
        w = Householder.calculate_w(matrix, column)
        wT = w.transpose()
                
        # calcula P'
        P2 = Matrix.eye(matrix.rows()-column-1, matrix.columns()-column-1)
        P2 = P2 - (2.0 / (wT * w)) * (w * wT)
        
        # acerta P
        for i in xrange(column + 1, P.rows()):
            for j in xrange(column + 1, P.columns()):
                P.set(i, j, P2.get(i-column-1, j-column-1))
        
        return P
    
    @staticmethod
    def execute(matrix):
        '''
        Executa o metodo para transformar a matrix numa matriz quase triangular superior ou numa tridiagonal
        @param Matrix
        @return Matrix
        '''
        result = matrix.copy()
        for i in xrange(result.columns() - 2):
            P = Householder.calculate_P(result, i)
            result = P * result * P
        return result