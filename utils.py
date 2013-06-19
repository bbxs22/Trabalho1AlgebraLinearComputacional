import properties

class Utils:

    @staticmethod
    def debug(message):
        '''
        Exibe mensagem para debug
        @str
        '''
        if properties.debug:
            print message
            
    @staticmethod
    def export(file_name, item):
        '''
        Exporta o item para um arquivo
        @param srt
        @param ???
        '''
        file = open(file_name, 'w')
        file.write(str(item))
        file.close()