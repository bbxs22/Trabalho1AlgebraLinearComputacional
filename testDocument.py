from document import *
import unittest

class TestDocumentMethods(unittest.TestCase):

    def test_remove_punctuation(self):
        new_document = Document.remove_punctuation('Wireless, Network System with Autonomous Antenna! Actuator; Control; for; Disaster... Information?')
        self.assertEqual(new_document, 'Wireless Network System with Autonomous Antenna Actuator Control for Disaster Information')
        
    def test_remove_stop_words(self):
        new_document = Document.remove_stopwords(['Wireless', 'Network', 'System', 'with', 'Autonomous', 'Antenna', 'Actuator', 'Control', 'for', 'Disaster', 'Information'])
        self.assertEqual(len(new_document), 9)
        self.assertEqual(new_document, ['Wireless', 'Network', 'System', 'Autonomous', 'Antenna', 'Actuator', 'Control', 'Disaster', 'Information'])
        
    def test_stemming_word(self):
        new_document = Document.stemming('Information')
        self.assertEqual(new_document, 'Informat')
        
    def test_stemming_words(self):
        new_document = Document.stemming(['Autonomous', 'Information', 'information'])
        self.assertEqual(new_document, ['Autonom', 'Informat', 'inform'])

    def test_prepare(self):
        new_document = Document.prepare('Wireless Network System with Autonomous Antenna Actuator Control for Disaster Information.')
        self.assertEqual(len(new_document), 8)
        self.assertEqual(new_document, ['wireless', 'network', 'autonom', 'antenna', 'actuat', 'control', 'disast', 'inform'])
        
    def test_prepare_multiple_whitespaces(self):
        new_document = Document.prepare('Wireless     Network System with   Autonomous Antenna    Actuator Control for Disaster Information.')
        self.assertEqual(len(new_document), 8)
        self.assertEqual(new_document, ['wireless', 'network', 'autonom', 'antenna', 'actuat', 'control', 'disast', 'inform'])

    def test_new_document(self):
        document = Document('123\n', 'Title\n', 'A novel technique for optimising the harmonics and reactive power under nonsinusoidal voltage conditions.\n')
        self.assertEqual(document.id, '123')
        self.assertEqual(document.title, 'Title')
        self.assertEqual(document.text, 'A novel technique for optimising the harmonics and reactive power under nonsinusoidal voltage conditions.')
        
    def test_tems(self):
        document = Document('123', '', 'A novel technique for optimising the harmonics and reactive power under nonsinusoidal voltage conditions.')
        terms = document.terms()
        self.assertEqual(len(terms), 9)
        self.assertEqual(terms, ['novel', 'techniqu', 'optimis', 'harmon', 'reactiv', 'power', 'nonsinusoid', 'voltag', 'condit'])
        
    def test_calculate_terms_frequency(self):
        document = Document('123', '', 'A novel technique for optimising the harmonics and reactive power under nonsinusoidal voltage conditions.')
        document.calculate_terms_frequency()
        terms_freq = document.terms_frequency()
        
        terms = ['novel', 'techniqu', 'optimis', 'harmon', 'reactiv', 'power', 'nonsinusoid', 'voltag', 'condit']
        terms.sort()
        terms_freq_keys = terms_freq.keys()
        terms_freq_keys.sort()
        self.assertEqual(terms_freq_keys, terms)
        
        for term in terms:
            self.assertEqual(type(terms_freq[term]), float)
            self.assertEqual(terms_freq[term], 1.0/9.0)
        

if __name__ == '__main__':
    unittest.main()