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

class EmptyStack(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.__stack = []

    def push(self, elem):
        self.__stack.append(elem)

    def pop(self):
        if not self.is_empty():
            return self.__stack.pop()
        raise EmptyStack("A pilha está vazia!")

    def is_empty(self):
        return  len(self.__stack) == 0

    def top(self):
        if self.is_empty():
            raise EmptyStack("A pilha está vazia!")
        return self.__stack[-1]

    def length(self):
        return len(self.__stack)

    def __str__(self):
        return self.__stack.__str__()

    def remove_all(self):
        self.__stack = []

    def remove_bar(self, tag):
        no_bar = ''
        for i in tag:
            if i != '/':
                no_bar += i
        return no_bar

    def is_matched_html(self, html):
        index = 0
        tamanho = len(html)

        while index < tamanho:

            if html[index] == '<':
                pos_fim_tag = index + 1
                while pos_fim_tag < tamanho and html[pos_fim_tag] != '>':
                    pos_fim_tag = index + 1

                if pos_fim_tag == tamanho:
                    return False

                conteudo_tag = html[index+1:pos_fim_tag]

                if conteudo_tag > tamanho and conteudo_tag[0] != '/':
                    self.push(conteudo_tag)
                else:
                    if self.is_empty():
                        return False

                conteudo_no_bar = self.remove_bar(conteudo_tag)

                if self.pop() != conteudo_no_bar:
                    return False

                index = pos_fim_tag + 1

            else:

                index += 1

        return self.is_empty()


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