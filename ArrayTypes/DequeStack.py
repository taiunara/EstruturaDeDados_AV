from ListaDeExercicios.ArrayTypes.ArrayDeque import ArrayDeque

class DequeStack:
    def __init__(self):
        self.__stack = ArrayDeque()

    def push(self, elem):
        self.__stack.add_last(elem)

    def pop(self):
        self.__stack.remove_last()

    def is_empty(self):
        return self.__stack.is_empty()

    def __str__(self):
        return self.__stack.__str__()