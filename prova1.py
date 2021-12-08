from node import Node


class Pilha:
    """Esta classe representa uma pilha usando uma estrutura encadeada."""

    def __init__(self):
        """ Construtor """
        self.top = None
        self._size = 0

    def __len__(self):
        """ Retorna o tamanho da lista """
        return self._size

    def push(self, elem):
        """Insere um elemento na pilha."""

        # Cria um novo nó com o dado a ser armazenado.
        node = Node(elem)

        # Faz com que o novo nó seja o topo da pilha.
        node.next = self.top

        # Faz com que o topo da pilha referencie o novo nó.
        self.top = node

        # Aumenta a pilha em uma unidade
        self._size = self._size + 1


    def pop(self):
        """Remove o elemento do topo da pilha."""
        if self._size > 0:
            node = self.top
            self.top = self.top.next

            # Diminui a pilha em uma unidade
            self._size = self._size - 1

            return node.data
        else:
            raise IndexError("A pilha está vazia")

    def peek(self):
        """ Retorna o topo da pilha sem remover """
        if self._size > 0:
            return self.top.data
        else:
            raise IndexError("A pilha está vazia")

    def __repr__(self):
        """ Dá uma representação desse objeto """
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

# Cria uma pilha vazia.
estacionamento = Pilha()
manobra = Pilha()
print("---------------------------------------------------")
print("------- Estacionamento Caminho Das Índias ---------")
print("---------------------------------------------------")
print()
print("Estacionamento vazio!")
print("Quantidade de carros: ", len(estacionamento))
print()

# Insere o primeiro elemento na pilha.
print("--------------- Sejam Bem-vindos! ----------------")
carro1 = str(input("Digite a placa do seu carro: "))
print()
print("---------- Seu carro está bem guardado -----------")
estacionamento.push([carro1, 0])
print()
print("Estacionamento")
print(estacionamento)
print("Quantidade de carros: ", len(estacionamento))
print()

# Verifica se o carro quer sair ou entrar
acao = str(input("Digite E para estacionar ou digite S para sair: "))
while acao == "S" or acao == "E":
    if acao == "E":
        print()
        print("--------------- Sejam Bem-vindos! ----------------")
        carroN = str(input("Digite a placa do seu carro: "))
        estacionamento.push([carroN, 0])
        print()
        print("---------- Seu carro está bem guardado -----------")
        print()
        print("Estacionamento")
        print(estacionamento)

    else:
        print("Posição dos carros:")
        print(estacionamento)
        placa = str(input("Digite a placa do seu carro: "))
        atual = estacionamento.top
        achou = False
        profundidade = 0
        while(atual):
            if placa == atual.data[0]:
                achou = True
                break
            atual = atual.next
            profundidade += 1
        if achou == True:
            for i in range(profundidade):
                carro = estacionamento.pop()
                carro[1] += 1
                manobra.push(carro)
                print("********** Manobrando os carros **********")
                print()
                print("Estacionamento")
                print(estacionamento)
                print("Manobra")
                print(manobra)
            carroEscolhido = estacionamento.pop()
            print()
            vez = "vez" if carroEscolhido[1] == 1 else "vezes" #Singular ou plural
            print("O carro {0} saiu e foi manobrado {1} {2}!".format(carroEscolhido[0],carroEscolhido[1],vez))
            print()
            
            for i in range(profundidade):
                print()
                print("********** Colocando os carros de volta **********")
                carro = manobra.pop()
                estacionamento.push(carro)
                print()
                print("Estacionamento")
                print(estacionamento)
                print("Manobra")
                print(manobra)
                print()
    print("Quantidade de carros: ", len(estacionamento))
    acao = str(input("Digite E para estacionar ou digite S para sair: "))