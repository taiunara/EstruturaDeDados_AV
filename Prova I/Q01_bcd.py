from ListaDeExercicios.ArrayTypes.AllArrays import ArrayQueue

class StreamingBuffer:
    def __init__(self, tamanho_max):
        self.buffer = ArrayQueue()
        self.tamanho_max = tamanho_max
        self.tamanho_atual = 0

    def receber_pacote(self, pacote):
        if self.tamanho_atual < self.tamanho_max:
            self.buffer.enqueue(pacote)
            self.tamanho_atual += 1
            print(f"O pacote: {pacote} foi recebido!")
        else:
            print(f'Tamanho limite já excedido! Pacote {pacote} foi descartado.')

    def reproduzir_proximo(self):
        if not self.buffer.is_empty():
            dado = self.buffer.dequeue()
            print(f"Reproduzindo {dado}")
            self.tamanho_atual -= 1

        else:
            print(f"Não há pacotes para reproduzir")


streamer = StreamingBuffer(2)
streamer.receber_pacote("Ep 02")
streamer.receber_pacote("Ep 05")

streamer.reproduzir_proximo()
streamer.reproduzir_proximo()
streamer.reproduzir_proximo()