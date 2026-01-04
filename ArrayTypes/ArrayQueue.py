class EmptyQueue(Exception):
    pass

class ArrayQueue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, elem):
        self.__queue.append(elem)

    def dequeue(self):
        if not self.is_empty():
            return self.__queue.pop(0)
        raise EmptyQueue('A fila está vazia!')

    def is_empty(self):
        return len(self.__queue) == 0

    def first(self):
        if self.is_empty():
            raise EmptyQueue('A fila está vazia!')
        return self.__queue[0]

    def __str__(self):
        return self.__queue.__str__()

    def remove_all(self):
        self.__queue = []