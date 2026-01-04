class ArrayDeque:
    def __init__(self):
        self.__deque = []

    def add_first(self, elem):
        self.__deque.insert(0, elem)

    def add_last(self, elem):
        self.__deque.append(elem)

    def remove_first(self):
        if not self.is_empty():
            return self.__deque.pop(0)
        else:
            return print(f"A lista está vazia")

    def remove_last(self):
        if not self.is_empty():
           return self.__deque.pop()
        else:
            return print(f"A lista está vazia")

    def is_empty(self):
        return len(self.__deque) == 0

    def __str__(self):
        return self.__deque.__str__()

    def first(self):
        if self.is_empty():
            print(f"A lista está vazia!")
        return self.__deque[0]

    def rotate(self):
       if not self.is_empty():
           primeiro = self.remove_first()
           self.add_last(primeiro)