from documents import *
from document import *
from matrix import *

def main(file_name):
    
    # inicia os documentos
    documents = Documents(file_name)
    
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
            # TF * IDF
            tf = document.terms_frequency(term)
            #idf = documents.inverse_document_frequency(term)
            #matrix.set(i, j, tf * idf)
            matrix.set(i, j, tf)
            j = j + 1
        i = i + 1
    
    # expoe a matrix num arquivo
    #file = open('terms.txt', 'w')
    #for term in list_terms:
    #    file.write(term)
    #    file.write('\n')
    #file.close()
    
    # expoe a matrix num arquivo
    file = open('matlab/matrix.txt', 'w')
    file.write(str(matrix.rows()))
    file.write('\n')
    file.write(str(matrix.columns()))
    file.write('\n')
    file.write(str(matrix))
    file.close()

if __name__ == '__main__':
    main('example.txt')