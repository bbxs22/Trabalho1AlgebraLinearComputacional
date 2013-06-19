import math
from vector import *

class Matrix:
    
    def __init__(self, values=[], rows=0, columns=0):
        self.__values = values
        self.__rows = rows
        self.__columns = columns
        
        # converte valores para float
        for i in xrange(len(self.__values)):
            self.__values[i] = float(self.__values[i])
            
    def rows(self):
        return self.__rows
        
    def columns(self):
        return self.__columns
        
    def get(self, row, column):
        return self.__values[row * self.__columns + column]
        
    def set(self, row, column, value):
        self.__values[row * self.__columns + column] = value
        
    @staticmethod
    def zeros(rows, columns):
        values = list()
        for row in xrange(rows * columns):
            values.append(0.0)
        return Matrix(values, rows, columns)
            
    @staticmethod
    def ones(rows, columns):
        values = list()
        for row in xrange(rows*columns):
            values.append(1.0)
        return Matrix(values, rows, columns)
        
    @staticmethod
    def eye(rows, columns):
        matrix = Matrix.zeros(rows, columns)
        for i in xrange(min(rows, columns)):
            matrix.set(i, i, 1.0)
        return matrix
        
    def copy(self):
        return Matrix(self.__values[:], self.rows(), self.columns())
        
    def transpose(self):
        matrix = Matrix(self.__values[:], self.columns(), self.rows())
        for i in xrange(self.rows()):
            for j in xrange(self.columns()):
                matrix.set(j, i, self.get(i, j))
        return matrix
        
    def norm(self):
        return math.sqrt(sum(map(lambda x: x**2, self.__values)))
        
    def get_row(self, index):
        start_position = index * self.columns()
        end_position = start_position + self.columns()
        if start_position < 0 or end_position > self.rows() * self.columns():
            raise ValueError('Invalid row')
        return Vector(self.__values[start_position : end_position], False)
        
    def tolist(self):
        array = list()
        for i in xrange(self.rows()):
            columns = self.__values[i * self.columns() : (i+1) * self.columns()]
            array.append(columns)
        return array
        
    def __sub__(self, matrix):
        if (self.rows() != matrix.rows() or self.columns() != matrix.columns()):
            raise ValueError('Sub error')
            
        result = self.copy()
        for i in xrange(self.rows()):
            for j in xrange(self.columns()):
                result.set(i, j, result.get(i, j) - matrix.get(i, j))
        return result
        
    def __rmul__(self, value):
        if (type(value) == int or type(value) == float):
            return self.__mul__(value)

    def __mul__(self, value):
        # multiplicacao por int / float
        if (type(value) == int or type(value) == float):
            result = self.copy()
            for i in xrange(self.rows()):
                for j in xrange(self.columns()):
                    result.set(i, j, result.get(i, j) * value)
            return result
        else:
            # multiplicacao de matrizes
            matrix = value
            result = Matrix.zeros(self.rows(), matrix.columns())
            for i in xrange(self.rows()):
                for k in xrange(matrix.columns()):
                    for j in xrange(self.columns()):
                            result.set(i, k, result.get(i, k) + self.get(i, j) * matrix.get(j, k))
            return result
            
    def __repr__(self):
        matrix = ''
        for i in xrange(self.rows()):
            for j in xrange(self.columns()):
                matrix += str(self.get(i, j)) + ' '
            matrix += '\n'
        return matrix
            