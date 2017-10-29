import threading, queue, time

class Posicao(threading.Thread):
    def __init__(self,mutex,fila_de_mesas,fila_de_posicao,tempo_de_espera):
        self.mutex = mutex
        self.fila_de_mesas = fila_de_mesas
        self.fila_de_posicao = fila_de_posicao
        self.tempo_de_espera = tempo_de_espera
        threading.Thread.__init__(self)

    def run(self):
            time.sleep(self.tempo_de_espera)
            with self.mutex:
                try:
                    data = self.fila_de_mesas.get(block=False)
                except queue.Empty:
                    pass
                else:
                    print(data)
                    data.setdefault('posicao X',0)
                    data.setdefault('posicao Y',0)
                    self.fila_de_posicao.put(data)

