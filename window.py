from Tkinter import *
from documents import *
from svd import *
import properties

class DocumentVO:
    
    def __init__(self, index, title, text, score):
        self.index = index
        self.title = title
        self.text = text
        self.score = score
        self.special_title = str(self.index) + '. ' + self.title
        if (score != None):
            self.special_title += '\n [SCORE = ' + str(self.score) + ']'

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
            self.list_docs.append(DocumentVO(i, document.title, document.text, None))
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
        
    def document(self, text):
        # posicao na lista
        position = int(text.split('.')[0])
        return self.list_docs[position]
        
    def list_documents(self):
        return self.list_docs

class App:

    def __init__(self, root, controller):
        self.controller = controller
        
        self.main_frame = Frame(root)
        self.main_frame.pack()

        frame_right = Frame(self.main_frame)
        frame_right.pack(side=RIGHT, fill=BOTH)

        frame_left = Frame(self.main_frame)
        frame_left.pack(side=LEFT, fill=BOTH)
        
        self.create_documents_area(frame_right)
        self.create_document_info_area(frame_left)
        
    def create_documents_area(self, parent):
        top_frame = Frame(parent)
        top_frame.pack(side=TOP)
        
        bottom_frame = Frame(parent, padx=15, pady=15)
        bottom_frame.pack(side=BOTTOM)
        
        label = Label(top_frame, text='Documentos')
        label.pack(side=TOP)
        
        help_frame = Frame(top_frame)
        help_frame.pack(side=BOTTOM, fill=BOTH)
        
        scroll = Scrollbar(help_frame)
        scroll.pack(side=RIGHT, fill=BOTH)

        self.documents_list = Listbox(help_frame, yscrollcommand=scroll.set, width=34)
        self.documents_list.bind('<<ListboxSelect>>', self.select_document)
        
        for document in self.controller.list_documents():
           self.documents_list.insert(END, document.special_title)

        self.documents_list.pack(side=LEFT, fill=BOTH)
        scroll.config(command=self.documents_list.yview)
        
        self.search_entry = StringVar()
        entry = Entry(bottom_frame, bd=5, width=30, textvariable=self.search_entry)
        entry.pack(side=LEFT)

        self.search_button = Button(bottom_frame, text="OK", command=self.search_action)
        self.search_button.pack(side=RIGHT)
        
    def create_document_info_area(self, parent):
        self.document_label = StringVar()
        label = Label(parent, textvariable=self.document_label)
        label.pack(side=TOP)
        
        bottom_frame = Frame(parent)
        bottom_frame.pack(side=BOTTOM)
        
        scroll = Scrollbar(bottom_frame)
        #scroll = Scrollbar(parent)
        scroll.pack(side=RIGHT, fill=BOTH)
        
        self.document_text = Text(bottom_frame, width=50, background='white')
        #self.document_text = Text(parent, background='white', state=DISABLED)
        self.document_text.configure(yscrollcommand=scroll.set)
        self.document_text.pack(side=LEFT)
        
    def select_document(self, event):
        widget = event.widget
        index = int(widget.curselection()[0])
        value = widget.get(index)
        
        document = self.controller.document(value)
        
        self.document_label.set(document.special_title)
        self.document_text.delete('1.0', '2.0')
        self.document_text.insert(END, document.text)
        
    def search_action(self):
        text = self.search_entry.get().strip()
        if text == '':
            self.controller.reset()
        else:
            self.controller.search(text)
        
        self.documents_list.delete(0, len(self.controller.list_documents()))
        
        for document in self.controller.list_documents():
           self.documents_list.insert(END, document.special_title)
    
root = Tk()
root.title('Trabalho Algebra Linear')
app = App(root, Controller(properties.input_file))
root.mainloop()

