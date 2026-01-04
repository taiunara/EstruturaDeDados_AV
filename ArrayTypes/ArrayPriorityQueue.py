class ArrayPriorityQueue:
    def __init__(self):
        self.__priority_queue = []

    # def add(self, priority, elem):
    #     self.__priority_queue.append((priority, elem))
    #     self.__priority_queue.sort()

    def add(self, priority, elem):
        if self.is_empty():
            self.__priority_queue.append((priority, elem))
            return

        # Procura a posição onde a chave deve ser inserida
        for pos in range(len(self.__priority_queue)):
            #“A prioridade que estou tentando colocar (5) é menor que a prioridade no índice 0 (1)?”
            #"Pegue o elemento na posição i da fila, e desse elemento, pegue a posição 0 da tupla (ou seja, a prioridade)"
            if priority < self.__priority_queue[pos][0]:
                self.__priority_queue.insert(pos, (priority, elem))
                return

        # Se não inseriu antes (maior que todas), adiciona no final
        self.__priority_queue.append((priority, elem))

    def remove_min(self):
        return self.__priority_queue.pop(0)

    def min(self):
        if not self.is_empty():
            return self.__priority_queue[0]
        return print(f'Está vazia!')

    def is_empty(self):
        return len(self.__priority_queue) == 0

    def __str__(self):
        return self.__priority_queue.__str__()