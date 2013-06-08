import math
from document import Document

class Documents:

    def __init__(self, file_name):
        # le os documentos
        file = open(file_name)
        lines = file.readlines()
        file.close()

        # cria lista de documentos
        self.__documents = list()
        for i in xrange(0, len(lines), 3):
            document = Document(lines[i], lines[i+1], lines[i+2])
            self.__documents.append(document)
            
        # cria conjunto de termos dos documentos
        self.__terms = set()
        for document in self.documents():
            self.__terms = self.__terms.union(document.terms())

    def documents(self):
        '''
        Documentos
        @return list<Document>
        '''
        return self.__documents
        
    def terms(self):
        '''
        Termos de todos os documentos
        @return set<str>
        '''
        return self.__terms
        
    def calculate_inverse_document_frequency(self):
        '''
        Calcula a frequencia do documento inversa
        Eh dada por:
            log (total_de_sentencas / total_de_sentencas_onde_o_termo_aparece)
        '''
        self.__inverse_document_frequency = dict.fromkeys(self.terms(), 0.0)
        
        for term in self.terms():
            # conta numero de documentos com o termo term
            count = 0.0
            for document in self.documents():
                if term in document.terms():
                    count += 1.0
            # calcula IDF
            self.__inverse_document_frequency[term] = math.log(len(self.documents()) / count, 10)
        
    def inverse_document_frequency(self, term=None):
        '''
        Frequencia do documento inversa de cada termo ou de um termo especifico
        @return dict<str, float>/float
        '''
        if term == None:
            return self.__inverse_document_frequency
        if self.__inverse_document_frequency.has_key(term):
            return self.__inverse_document_frequency[term]
        else:
            return float("inf")
