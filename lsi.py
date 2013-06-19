from matrix import *
from numpy import linalg
from utils import *
import properties

class LSI:

    @staticmethod
    def prepare_matrix(documents):
        '''
        Cria a matriz com as informacoes de termos nos documentos
        @param Documents
        @return Matrix
        '''
        # calcula TF
        for document in documents.documents():
            document.calculate_terms_frequency()
            
        # calcula IDF
        documents.calculate_inverse_document_frequency()
        
        # cria lista de termos e documentos
        list_terms = documents.terms()
        list_documents = documents.documents()
        
        # cria a matriz esparsa
        m = len(list_terms)
        n = len(list_documents)
        matrix = Matrix.ones(m, n)
        
        # popula matriz
        i = 0
        for term in list_terms:
            j = 0
            for document in list_documents:
                tf = document.terms_frequency(term)
                matrix.set(i, j, tf)
                
                # TF * IDF
                if (properties.frequency == 'tfidf'):
                    idf = documents.inverse_document_frequency(term)
                    matrix.set(i, j, tf * idf)
                    
                j = j + 1
            i = i + 1
        
        return matrix

    def __init__(self, documents):
        # prepara a matriz
        self.matrix = LSI.prepare_matrix(documents)
        
        # SVD
        self.u, self.s, self.v = LSI.calculate_svd(self.matrix)
        
        # calcula o score vector
        values = list()
        for i in xrange(self.s.rows()):
            values.append(self.s.get(i))
        self.score_vector = Vector(values, False)
        
        # expoe as matrizes num arquivo
        Utils.export(properties.matrix_file, self.matrix)
        Utils.export(properties.matrix_u_file, self.u)
        Utils.export(properties.matrix_s_file, self.s)
        Utils.export(properties.matrix_v_file, self.v)
        
    @staticmethod
    def calculate_svd(matrix, k=2):
        '''
        Calcula as matrizes U, S e V da decomposicao em valores singulares de uma matriz com rank k.
        Tal decomposicao transforma a matriz no produto de tres matrizes: U . S . V^T
        @param Matrix
        @param int (optional)
        @return tuple<Matrix, Vector, Matrix>
        '''
        # calcula SVD
        u, s, vT = linalg.svd(matrix.tolist())
        u = u.tolist()
        s = s.tolist()
        v = vT.transpose().tolist()
        
        # mantem apenas os k melhores auto valores e auto vetores        
        matrix_u = list()
        for i in xrange(matrix.rows()):
            matrix_u += u[i][0:k]
        matrix_u = Matrix(matrix_u, matrix.rows(), k)
        
        matrix_v = list()
        for i in xrange(matrix.columns()):
            matrix_v += v[i][0:k]
        matrix_v = Matrix(matrix_v, matrix.columns(), k)
        
        vector_s = Vector(s[0:k])
        
        return matrix_u, vector_s, matrix_v
        
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
        
    def calculate_score_cosine(self, query_vector, matrix):
        '''
        Recupera o vetor de score usando co-seno
        @param Vector
        @param Matrix
        @return Vector
        '''        
        product = 0.0
        xsLengthSquared = 0.0;
        ysLengthSquared = 0.0;
        
        # recupera os vetores-linha da matriz
        vectors = self.get_row_vectors(matrix)
            
        # ajusta o score de 0 para cada um dos termos
        scores = Vector([0.0] * len(vectors))
        
        # caso nao haja termo valido na query, nao executa os calculos
        if query_vector.norm() == 0:
            return scores
            
        # calcula o score para cada elemento de vector
        s = 0
        for vector in vectors:
            for i in xrange(query_vector.columns()):
                sqrtScale = math.sqrt(self.score_vector.get(i))
                scaledXs = sqrtScale * query_vector.get(i);
                scaledYs = sqrtScale * vector.get(i);
                
                xsLengthSquared += scaledXs * scaledXs
                ysLengthSquared += scaledYs * scaledYs
                product += scaledXs * scaledYs
                
            scores.set(s, product / math.sqrt(xsLengthSquared * ysLengthSquared))
            s = s + 1 
        
        return scores
        
    def calculate_score_dot(self, query_vector, matrix):
        '''
        Recupera o vetor de score usando produto interno
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
    
    def calculate_score(self, query_vector, matrix):
        '''
        Recupera o vetor de score
        @param Vector
        @param Matrix
        @return Vector
        '''
        if properties.score == 'cosine':
            return self.calculate_score_cosine(query_vector, matrix)
        
        if properties.score == 'dot':
            return self.calculate_score_dot(query_vector, matrix)
        
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