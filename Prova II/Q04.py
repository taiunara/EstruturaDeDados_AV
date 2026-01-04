class list_decompressor:

    def _init_(self, lista):
        self._lista = lista


    def next(self):
        aux = self._lista

        while aux and aux[0] == 0:
            aux.pop(0)
            aux.pop(0)

        if not aux:
            return None

        aux[0] -= 1
        return aux[1]