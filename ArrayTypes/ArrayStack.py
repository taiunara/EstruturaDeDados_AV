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















    # def remove_bar(self, tag):
    #     tag_formatada = ""
    #     for i in tag:
    #         if i != '/':
    #             tag_formatada += i
    #     return tag_formatada
    #
    # def is_matched_html(self, html):
    #     index = 0
    #     tamanho = len(html)
    #
    #     while index < tamanho:
    #         if html[index] == "<":
    #             posicao_fecha_tag = index + 1
    #
    #             while posicao_fecha_tag < tamanho and html[posicao_fecha_tag] != ">":
    #                 posicao_fecha_tag += 1
    #
    #             if posicao_fecha_tag == tamanho:
    #                 return False
    #
    #             conteudo_tag = html[index + 1: posicao_fecha_tag]
    #
    #             if len(conteudo_tag) > 0 and conteudo_tag[0] != "/":
    #                 self.push(conteudo_tag)
    #             else:
    #                 if self.is_empty():
    #                     return False
    #
    #                 conteudo_sem_barra = self.remove_bar(conteudo_tag)
    #
    #                 if self.pop() != conteudo_sem_barra:
    #                     return False
    #
    #             index = posicao_fecha_tag + 1
    #
    #         else:
    #             index += 1
    #
    #     return self.is_empty()