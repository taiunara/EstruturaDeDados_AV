class FlattenIterator:
    def __init__(self, lista):
        self.pilha = [iter(lista)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.pilha:
            atual = self.pilha[-1]
            try:
                valor = next(atual)
                if isinstance(valor, int):
                    return valor
                else:
                    self.pilha.append(iter(valor))
            except StopIteration:
                self.pilha.pop()
        raise StopIteration

    def __str__(self):
        return self.pilha.__str__()


lista = [1, [2, [3, 4], 5], 6]

it = FlattenIterator(lista)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 4
print(next(it))  # 5
print(next(it))  # 6
