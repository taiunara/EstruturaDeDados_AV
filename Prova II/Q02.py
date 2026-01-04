from ListaDeExercicios.ArrayTypes.AllArrays import ArrayStack


def validar_parentes(expressao: str):
    pilha = ArrayStack()
    pares = {')':'(', ']':'[', '}':'{'}

    for char in expressao:
        if char in '([{':
            pilha.push(char)
        elif char in ')]}':
            if pilha.is_empty():
                return False
            topo = pilha.pop()
            if topo != pares[char]:
                return  False

    return pilha.is_empty()

print(validar_parentes("{[2*(3+1)]}"))
print(validar_parentes("{[2*(3+1])}"))
print(validar_parentes("((AB)"))

