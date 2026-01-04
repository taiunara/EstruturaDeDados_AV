from ListaDeExercicios.ArrayTypes.AllArrays import ArrayStack

def avaliar_rpn(expression: list):

    stack = ArrayStack()

    ops = {
        "+": lambda x,y: x + y,
        "-": lambda x,y: x - y,
        "*": lambda x,y: x * y,
        "/": lambda x,y: x / y
    }

    for token in expression:
        if token.isdigit():
            stack.push(int(token))
        else:
            y = stack.pop()
            x = stack.pop()
            resultado = ops[token](x,y)
            stack.push(resultado)

    return stack.pop()


print(avaliar_rpn(["2", "3", "+", "4", "*"]))


























#def avaliar_rpn(expressao: list):
#     pilha = ArrayStack()
#
#     ops = {
#         '+': lambda x, y: x + y,
#         '-': lambda x, y: x - y,
#         '*': lambda x, y: x * y,
#         '/': lambda x, y: x / y
#     }
#
#     for token in expressao:
#         if token.isdigit():
#             pilha.push(int(token))
#         else:
#             y = pilha.pop()
#             x = pilha.pop()
#             resultado = ops[token](x, y)
#             pilha.push(resultado)
#
#     return pilha.pop()