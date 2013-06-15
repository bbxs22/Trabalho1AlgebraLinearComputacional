import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade
from documents import *
from svd import *
import properties

class DocumentVO:
    
    def __init__(self, index, title, text, score):
        self.index = index
        self.title = title
        self.text = text
        self.score = score
        
    def get_values(self):
        return [self.index, self.score, self.title]

class Controller:
    
    def __init__(self, file_name):
        # inicia os documentos
        self.documents = Documents(file_name)
        
        # calcula as matrizes U, S e V (matlab)
        self.svd = SVD()
        
        # inicializa a lista de documentos
        self.reset()
        
    def reset(self):
        documents = self.documents.documents()
        i, self.list_docs = 0, list()
        for document in documents:
            self.list_docs.append(DocumentVO(i, document.title, document.text, 0.0))
            i = i + 1
        
    def search(self, text):
        # somente para debug
        print 'QUERY'
        print text
        print 'ALL TERMS'
        print self.documents.terms()
        
        # inicia analise buscando os termos que estao sendo procurados
        terms = self.documents.find_terms(text)
        print 'FOUND AT'
        print terms        
        
        # calcula o vetor de consulta
        query_vector = self.svd.get_query_vector(terms)
        print 'QUERY_VECTOR'
        print query_vector
        
        # score dos documentos para a consulta
        doc_score = self.svd.calculate_score(query_vector, self.svd.v)
        print 'DOC_SCORE'
        print doc_score
        
        # score dos termos para a consulta
        term_score = self.svd.calculate_score(query_vector, self.svd.u)
        print 'TERM_SCORE'
        print term_score
        
        # cria lista de documentos
        documents = self.documents.documents()
        i, self.list_docs = 0, list()
        for document in documents:
            self.list_docs.append(DocumentVO(i, document.title, document.text, doc_score.get(i)))
            i = i + 1
                    
    def document(self, position):
        # posicao na lista
        return self.list_docs[position]
        
    def list_documents(self):
        return self.list_docs

class MainWindowGTK:

    COLUMNS = [(0, 'Id'), (1, 'Score'), (2, 'Titulo')]

    def __init__(self, controller):
        self.controller = controller
        
        filename = "main_window.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(filename)
        self.builder.connect_signals(self)
        
        self.__prepare_main_window()
        self.__prepare_search_entry()
        self.__prepare_search_button()
        self.__prepare_document_title_label()
        self.__prepare_document_text_label()
        self.__prepare_documents_treeview()
        
        self.__prepare_properties_window()
        
    def __prepare_main_window(self):
        '''
        Prepara main_window
        Conecta evento de 'destroy'
        '''
        self.window = self.builder.get_object("main_window")
        if (self.window):
            self.window.connect("destroy", gtk.main_quit)
            
    def hello(self, widget):
        print "HELLO"
            
    def __prepare_search_entry(self):
        '''
        Prepara search_entry
        '''        
        self.search_entry = self.builder.get_object("search_entry")
        
    def __prepare_search_button(self):
        '''
        Prepara search_button
        Conecta evento de 'clicked'
        '''
        self.search_button = self.builder.get_object("search_button")
        if (self.search_button):
            self.search_button.connect("clicked", self.search)

    def __prepare_document_title_label(self):
        '''
        Prepara document_title_label
        '''
        self.document_title_label = self.builder.get_object("document_title_label")

            
    def __prepare_document_text_label(self):
        '''
        Prepara document_text_label
        '''
        self.document_text_label = self.builder.get_object("document_text_label")
        
    def __prepare_documents_treeview(self):
        '''
        Prepara documents_treeView
        '''
        self.documents_list = gtk.ListStore(int, float, str)
        self.documents_view = self.builder.get_object("documents_treeview")
        if (self.documents_view):
            self.documents_view.set_model(self.documents_list)
            self.documents_view.connect("row-activated", self.select)

        # prepara colunas
        for column_id, column_title in MainWindowGTK.COLUMNS:
            column = gtk.TreeViewColumn(column_title, gtk.CellRendererText(), text=column_id)
            column.set_resizable(True)
            column.set_sort_column_id(column_id)
            self.documents_view.append_column(column)
            
        # inicializa
        self.load_documents()
        
    def __prepare_properties_window(self):
        '''
        Prepara properties_window
        Conecta evento de 'destroy'
        '''
        self.properties_window = self.builder.get_object("properties_window")
        if (self.properties_window):
            self.properties_window.connect("destroy", gtk.main_quit)
        
    def load_documents(self):
        '''
        Carrega os documentos da documents_treeView
        '''
        self.documents_list.clear()
        for document in self.controller.list_documents():
            self.documents_list.append(document.get_values())
            
    def select(self, widget, path, view_column):
        model, iter = widget.get_selection().get_selected()
        document_id = model.get_value(iter, 0)
        document = self.controller.document(document_id)
        
        self.document_title_label.set_text(document.title)
        self.document_text_label.set_text(document.text)
        
    def search(self, widget):
        text = self.search_entry.get_text().strip()
        if text == '':
            self.controller.reset()
        else:
            self.controller.search(text)
        
        self.load_documents()

if __name__ == "__main__":
    hwg = MainWindowGTK(Controller(properties.input_file))
    gtk.main()