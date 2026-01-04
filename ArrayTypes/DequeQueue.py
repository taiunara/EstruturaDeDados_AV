from ListaDeExercicios.ArrayTypes.ArrayDeque import ArrayDeque

class DequeQueue:
    def __init__(self):
        self.__deque = ArrayDeque()

    def enqueue(self, elem):
        self.__deque.add_last(elem)

    def dequeue(self):
        if self.__deque.is_empty():
            raise Exception("Fila vazia")
        else:
            return self.__deque.remove_first()

    def is_empty(self):
        return self.__deque.is_empty()

    def __str__(self):
        return self.__deque.__str__()