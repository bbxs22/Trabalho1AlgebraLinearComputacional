from documents import *
from svd import *
import properties

def main(file_name):
    
    # inicia os documentos
    documents = Documents(file_name)
        
    # cria lista de termos e documentos
    list_terms = documents.terms()
    list_documents = documents.documents()
    print 'TERMS'
    print list_terms
    
    # calcula as matrizes U, S e V (matlab)
    svd = SVD()
    
    # inicia analise
    terms = documents.find_terms(properties.find_terms)
    print 'FOUND AT'
    print terms
    
    query_vector = svd.get_query_vector(terms)
    print 'QUERY_VECTOR'
    print query_vector
    
    # score dos documentos para a consulta
    print 'DOC_SCORE'
    print svd.calculate_score(query_vector, svd.v)
    
    # score dos termos para a consulta
    print 'TERM_SCORE'
    print svd.calculate_score(query_vector, svd.u)

if __name__ == '__main__':
    main(properties.input_file)