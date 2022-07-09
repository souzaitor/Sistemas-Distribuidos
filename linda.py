"""Linda Tuple Space 

Implementação da classe de um Tuple Space
Linda. O modelo Linda suporta um armazenamento de 
memória compartilhada chamado espaço de tupla para 
comunicação entre os processos de aplicativos. Os 
espaços de tupla podem ser acessados por operações 
simples.

Exemplo:
out topico ze mensagem 1
Cria no espaço tupla um tópico com nome "topico" de autor "ze" e mensagem "mensagem 1"

rd topico
Lê no espaço tupla o topico de nome "topico"

in topico ze mensagem 1
Deleta a mensagem "mensagem 1" de autor "ze" no tópico "topico" e exibe a mensagem
"""
class Linda:

    def __init__(self):
        self.tupleSpace = {}

    """
    Comando out: Adiciona uma tupla no tuple space
    """
    def _out(self, thread, autor, dados):
        if(self.tupleSpace.get(thread)):
            self.tupleSpace[thread].append({"autor": autor, "dados": dados})
            return "Uma thread foi atualizada"
        else:
            self.tupleSpace[thread] = []
            self.tupleSpace[thread].append({"autor": autor, "dados": dados})
            return "Uma nova thread foi criada"
    
    """
    Comando in: tenta combinar alguma tupla 
    no espaço da tupla, se uma correspondência 
    for encontrada, remove do espaço da tupla
    """
    def _in(self, thread, autor, dados):
        removido = False

        for x in range(0, self.tupleSpace[thread].__len__()):
            if(self.tupleSpace[thread][x]["autor"] == autor and self.tupleSpace[thread][x]["dados"] == dados):
               removido = self.tupleSpace[thread][x]
               self.tupleSpace[thread].pop(x)
               break

        if(not removido):
            return "Não foi removida, tupla inválida"

        else:
            return str(removido)
            
    """
    Comando read: se subscreve em algum tema e exibe todas as mensagens
    Semelhante a in, exceto que a tupla combinada permanece no tuple space
    A thread de execução é suspensa se não corresponder a uma tupla
    """
    def _rd(self, thread):
        if(self.tupleSpace.get(thread)):
            return str(self.tupleSpace[thread])
        else:
            return "Falha ao retornar uma thread"
