from dequeue import Dequeue

class Stack(Dequeue):
    def __init__(self, max):
        super().__init__(max)

    def push(self,elemento):
        if self.offerFirst(elemento):
            
            return "Elemento inserido com sucesso"
        else:
            return "Erro ao inserir elemento no Stack" 

    def pop(self):
        if not self.empty():
            return self.pollFirst()
        else:
            return "A queue está vazia"

    def peek(self):
        if not self.empty():
            return self.peekFirst()
        else:
            return "Nenhum, a queue está vazia"

    def empty(self):
        if not self.size():
            return True
        else:
            return False


def menu():
    print('-------------------------------------------------------')
    print(f'1 - inserir elemento')
    print(f'2 - remover e retornar o elemento no topo')
    print(f'3 - mostra elemento no topo da stack')
    print(f'4 - numero de elementos na stack')
    print(f'5 - ver se a stack está vazia')
    print(f'6 - encerrar ')


def main():
    tam = int(input('qual o tamanho da Stack desejada? '))
    stack = Stack(tam)
    while True:
        menu()
        opcao = input('qual a operação desejada? ')

        match opcao:
            case '1':
                elemento = input("informe o elemento a ser inserido: ")
                print(stack.push(elemento))

            case '2':
                print(f'Elemento retirado: {stack.pop()}') 
            
            case '3':
                print(f"Elemento no topo: {stack.peek()}")
            
            case '4':
                print(f"Tamanho da Stack: {stack.size()}")
            
            case'5':
                if stack.empty():
                    print(" A queue está vazia")
                else:
                    print("Existem elementos na queue")
            case '6':
                break

            case _:
                print("Comando desconhecido")

if __name__ == '__main__':
    main()