from sentence import *
import unittest

class TestSentenceMethods(unittest.TestCase):

    def test_remove_punctuation(self):
        new_sentence = Sentence.remove_punctuation('Wireless, Network System with Autonomous Antenna! Actuator; Control; for; Disaster... Information?')
        self.assertEqual(new_sentence, 'Wireless Network System with Autonomous Antenna Actuator Control for Disaster Information')
        
    def test_remove_stop_words(self):
        new_sentence = Sentence.remove_stopwords(['Wireless', 'Network', 'System', 'with', 'Autonomous', 'Antenna', 'Actuator', 'Control', 'for', 'Disaster', 'Information'])
        self.assertEqual(len(new_sentence), 9)
        self.assertEqual(new_sentence, ['Wireless', 'Network', 'System', 'Autonomous', 'Antenna', 'Actuator', 'Control', 'Disaster', 'Information'])
        
    def test_stemming_word(self):
        new_sentence = Sentence.stemming('Information')
        self.assertEqual(new_sentence, 'Informat')
        
    def test_stemming_words(self):
        new_sentence = Sentence.stemming(['Autonomous', 'Information', 'information'])
        self.assertEqual(new_sentence, ['Autonom', 'Informat', 'inform'])

    def test_prepare(self):
        new_sentence = Sentence.prepare('Wireless Network System with Autonomous Antenna Actuator Control for Disaster Information.')
        self.assertEqual(len(new_sentence), 8)
        self.assertEqual(new_sentence, ['wireless', 'network', 'autonom', 'antenna', 'actuat', 'control', 'disast', 'inform'])
        
    def test_prepare_multiple_whitespaces(self):
        new_sentence = Sentence.prepare('Wireless     Network System with   Autonomous Antenna    Actuator Control for Disaster Information.')
        self.assertEqual(len(new_sentence), 8)
        self.assertEqual(new_sentence, ['wireless', 'network', 'autonom', 'antenna', 'actuat', 'control', 'disast', 'inform'])
        
    def test_tems(self):
        sentence = Sentence('A novel technique for optimising the harmonics and reactive power under nonsinusoidal voltage conditions.')
        terms = sentence.terms()
        self.assertEqual(len(terms), 9)
        self.assertEqual(terms, ['novel', 'techniqu', 'optimis', 'harmon', 'reactiv', 'power', 'nonsinusoid', 'voltag', 'condit'])
        
    def test_calculate_terms_frequency(self):
        sentence = Sentence('A novel technique for optimising the harmonics and reactive power under nonsinusoidal voltage conditions.')
        sentence.calculate_terms_frequency()
        terms_freq = sentence.terms_frequency()
        
        terms = ['novel', 'techniqu', 'optimis', 'harmon', 'reactiv', 'power', 'nonsinusoid', 'voltag', 'condit']
        self.assertEquals(terms_freq.keys().sort(), terms.sort())
        
        for term in terms:
            self.assertEquals(type(terms_freq[term]), float)
            self.assertEquals(terms_freq[term], 1.0/9.0)
        

if __name__ == '__main__':
    unittest.main()