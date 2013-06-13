from documents import *
import unittest

class TestDocumentsMethods(unittest.TestCase):
    
    def test_new_documents(self):
        documents = Documents('test/documents/test_new_documents.txt')
        list_docs = documents.documents()
        self.assertEqual(len(list_docs), 7)
        self.assertEqual(list_docs[0].id, '1185384')
        self.assertEqual(list_docs[1].id, '5718383')
        self.assertEqual(list_docs[2].id, '5718384')
        self.assertEqual(list_docs[3].id, '6185384')
        self.assertEqual(list_docs[4].id, '6315383')
        self.assertEqual(list_docs[5].id, '6315384')
        self.assertEqual(list_docs[6].id, '6325384')
        
    def test_terms(self):
        documents = Documents('test/documents/test_terms.txt')
        self.assertEqual(len(documents.documents()), 3)

        doc_terms = list(documents.terms())
        doc_terms.sort()
        self.assertEqual(len(doc_terms), 10)
        
        terms = ['disast', 'japan', 'number', 'natur', 'earthquak', 'tsunami', 'repres', 'east', 'great', '2011']
        terms.sort()
        self.assertEqual(doc_terms, terms)
        
    def test_calculate_inverse_document_frequency_all_words_in_all_documents(self):
        documents = Documents('test/documents/test_calculate_inverse_document_frequency_all_words_in_all_documents.txt')        
        documents.calculate_inverse_document_frequency()
        inv_doc_freq = documents.inverse_document_frequency()
        
        terms = ['disast', 'japan', 'number', 'natur', 'earthquak', 'tsunami', 'repres', 'east', 'great', '2011']
        terms.sort()
        inv_doc_freq_keys = inv_doc_freq.keys()
        inv_doc_freq_keys.sort()
        self.assertEqual(inv_doc_freq_keys, terms)
        
        for term in terms:
            self.assertEqual(type(inv_doc_freq[term]), float)
            self.assertAlmostEqual(inv_doc_freq[term], 0.0, delta=0.000001)
            
    def test_calculate_inverse_document_frequency_no_word_in_all_documents(self):
        documents = Documents('test/documents/test_calculate_inverse_document_frequency_no_word_in_all_documents.txt')        
        documents.calculate_inverse_document_frequency()
        inv_doc_freq = documents.inverse_document_frequency()
        
        terms = ['disast', 'japan', 'number', 'natur', 'earthquak', 'tsunami', 'repres', 'east', 'great', '2011', 'softwar', 'size', 'estim', 'key', 'entir', 'program', 'accur', 'affect', 'success', 'project', 'immedi']
        terms.sort()
        inv_doc_freq_keys = inv_doc_freq.keys()
        inv_doc_freq_keys.sort()
        self.assertEqual(inv_doc_freq_keys, terms)
        
        for term in terms:
            self.assertEqual(type(inv_doc_freq[term]), float)
            self.assertAlmostEqual(inv_doc_freq[term], 0.301029, delta=0.000001)
            
    def test_terms_inverse_document_frequency(self):
        documents = Documents('test/documents/test_terms_inverse_document_frequency.txt')
        documents.calculate_inverse_document_frequency()
        self.assertEqual(type(documents.inverse_document_frequency()), dict)
        self.assertEqual(type(documents.inverse_document_frequency('term')), float)
        self.assertAlmostEqual(documents.inverse_document_frequency('novel'), float("inf"), delta=0.000001)
        self.assertAlmostEqual(documents.inverse_document_frequency('number'), 0.301029, delta=0.000001)
        
    def test_find_terms(self):
        documents = Documents('test/documents/test_find_terms.txt')
        positions = documents.find_terms('Human')
        self.assertEqual(type(positions), list)
        self.assertEqual(len(positions), 1)
        self.assertEqual(positions[0], 9)
        self.assertEqual(documents.terms()[9], 'human')
        
        positions = documents.find_terms('Human another')
        self.assertEqual(type(positions), list)
        self.assertEqual(len(positions), 1)
        self.assertEqual(positions[0], 9)
        self.assertEqual(documents.terms()[9], 'human')
        
        positions = documents.find_terms('Human comp')
        self.assertEqual(type(positions), list)
        self.assertEqual(len(positions), 2)
        self.assertEqual(positions[0], 9)
        self.assertEqual(positions[1], -1)
        self.assertEqual(documents.terms()[9], 'human')
        
        positions = documents.find_terms('Human computer')
        self.assertEqual(type(positions), list)
        self.assertEqual(len(positions), 2)
        self.assertEqual(positions[0], 9)
        self.assertEqual(positions[1], 3)
        self.assertEqual(documents.terms()[3], 'comput')
        self.assertEqual(documents.terms()[9], 'human')

if __name__ == '__main__':
    unittest.main()