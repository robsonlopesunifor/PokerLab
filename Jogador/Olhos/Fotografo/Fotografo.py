import threading, queue, time

class Fotografo(threading.Thread):
    def __init__(self,mutex,fila_de_posicao,tempo_de_espera):
        print('| __init__ > INICIO')
        self.mutex = mutex
        self.tempo_de_espera = tempo_de_espera
        self.fila_de_posicao = fila_de_posicao
        threading.Thread.__init__(self)
        print('| __init__ > FIM')

    def run(self):
            print('| run > INICIO')
            time.sleep(self.tempo_de_espera)
            with self.mutex:
                try:
                    data = self.fila_de_posicao.get(block=False)
                except queue.Empty:
                    pass
                else:
                    print(data)
            print('| run > FINAL')

