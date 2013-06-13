from matrix import *

class SVD:

    MATLAB_U = 'matlab/u.txt'
    MATLAB_S = 'matlab/s.txt'
    MATLAB_V = 'matlab/v.txt'

    @staticmethod
    def read_matrix(file_name):
        '''
        Le a matriz de um arquivo
        @param str
        @return Matrix
        '''
        temp, rows, values = list(), 0, list()
        file = open(file_name)
        for line in file:
            temp = map(float, line.split())
            values += temp
            rows = rows + 1
        return Matrix(values, rows, len(temp))

    def __init__(self):
        self.u = SVD.read_matrix(SVD.MATLAB_U)
        self.s = SVD.read_matrix(SVD.MATLAB_S)
        self.v = SVD.read_matrix(SVD.MATLAB_V)
        
        values = list()
        for i in xrange(self.s.rows()):
            values.append(self.s.get(i, i))
        self.score_vector = Vector(values, False)
        
    def get_query_vector(self, terms_position):
        '''
        Recupera o vetor correspondente a consulta
        O vetor consulta eh dado pela soma coordenada a coordenada de cada vetor coluna que representa o termo
        @param list<int>
        @return Vector
        '''
        size = self.u.columns()
        query_vector = Vector([0.0]*size, False)
        
        for position in terms_position:
            if position > 0:
                query_vector = query_vector + self.u.get_row(position)
            
        return query_vector
        
    def calculate_score(self, query_vector, matrix):
        '''
        Recupera o vetor de score
        @param Vector
        @param Matrix
        @return Vector
        '''
        # recupera os vetores-linha da matriz
        vectors = self.get_row_vectors(matrix)
            
        # ajusta o score de 0 para cada um dos termos
        scores = Vector([0.0] * len(vectors))
            
        # calcula o score para cada elemento de vector
        s = 0
        for vector in vectors:
            for i in xrange(query_vector.columns()):
                score = query_vector.get(i) * vector.get(i) * self.score_vector.get(i)
                scores.set(s, scores.get(s) + score)
            s = s + 1 
        
        return scores
        
    def get_row_vectors(self, matrix):
        '''
        Recupera a lista de vetores linha da matriz
        @param Matrix
        @return list<Vector>
        '''
        vectors = list()
        for i in xrange(matrix.rows()):
            vectors.append(matrix.get_row(i))
        return vectors