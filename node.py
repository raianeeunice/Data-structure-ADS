class Node:
    """Esta classe representa um nó de uma estrutura encadeada."""
    def __init__(self, data=0):
        """ O valor de fato """
        self.data = data

        """ A posição do próximo na pilha """
        self.next = None

