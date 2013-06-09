def main(file_name):
    
    # inicia os documentos
    documents = Documents(file_name)
    
    # calcula TF
    for document in documents.document():
        document.calculate_terms_frequency()
        
    # calcula IDF
    documents.calculate_inverse_document_frequency()
    
    # cria a matriz esparsa
    matrix = list()
    for term in documents.terms():
        row = list()
        for document in documents.documents()
            # TF * IDF
            tf = document.terms_frequency(term)
            idf = documents.inverse_document_frequency(term)
            row.append(td * idf)
        matrix.append(row)
    

if __name__ == '__main__':
    main('article')