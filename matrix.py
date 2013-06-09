import math

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
        
    def __sub__(self, matrix):
        if (self.rows() != matrix.rows() or self.columns() != matrix.columns()):
            raise ValueError('Mult error')
            
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
                            result.set(i, k, result.get(i, k) + self.get(i, j) * matrix.get(j, k));
            return result