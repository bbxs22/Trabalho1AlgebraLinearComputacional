from documents import *
from svd import *

def main(file_name):
    
    # inicia os documentos
    documents = Documents(file_name)
        
    # cria lista de termos e documentos
    list_terms = documents.terms()
    list_documents = documents.documents()
    
    # calcula as matrizes U, S e V (matlab)
    svd = SVD()
    
    # inicia analise
    terms = documents.find_terms('book')
    query_vector = svd.get_query_vector(terms)
    
    # score dos documentos para a consulta
    print svd.calculate_score(query_vector, svd.v)
    
    # score dos termos para a consulta
    print svd.calculate_score(query_vector, svd.u)

if __name__ == '__main__':
    main('example.txt')