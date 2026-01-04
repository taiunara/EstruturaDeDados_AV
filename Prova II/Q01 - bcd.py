from ListaDeExercicios.ArrayTypes.AllArrays import ArrayPriorityQueue


class TriagemHospitalar:
    def __init__(self, tamanho):
        self._tamanho = tamanho
        self.priority_queue = ArrayPriorityQueue()
        self.qde_pacientes = 0

    def adicionar_paciente(self, nome: str, prioridade: int):
        if self.qde_pacientes < self._tamanho:
            self.priority_queue.add(prioridade, nome)
            print(f'Paciente: {nome} adicionado na fila, aguarde atendimento')
            self.qde_pacientes += 1
        else:
            print(f"A sala de espera está com a lotação máxima. {nome}, busque outro lugar para o atendimento")

    def chamar_proximo(self):
        if not self.priority_queue.is_empty():
            paciente =  self.priority_queue.remove_min()
            print(f'Paciente {paciente} foi atendido(a)')
            self._tamanho -= 1
        else:
            print('Não há pacientes para serem atendidos.')

triagem = TriagemHospitalar(3)

triagem.adicionar_paciente("Luiza", 1)
triagem.adicionar_paciente("Jucy", 5)
triagem.adicionar_paciente("Marcos", 2)
triagem.adicionar_paciente("Léo", 2)

triagem.chamar_proximo()
triagem.chamar_proximo()
triagem.chamar_proximo()
triagem.chamar_proximo()


