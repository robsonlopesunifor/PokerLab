import threading, queue, time
from Olhos.Posicao import Posicao
from Olhos.Fotografo import Fotografo



if __name__ == '__main__':

    numemensagens = 4

    fila_de_mesas = queue.Queue()
    fila_de_posicao = queue.Queue()

    fila_de_mesas.put({'Titulo da Janela':'Threading - Bloco de notas'})
    fila_de_mesas.put({'Titulo da Janela':'Nomeado - Bloco de notas'})
    fila_de_mesas.put({'Titulo da Janela':'Queue - Bloco de notas'})
    fila_de_mesas.put({'Titulo da Janela':'Threading - Bloco de notas'})

    stdoutmutex = threading.Lock()

    posicoes = []

    for i in range(4):
        thread = Posicao.Posicao(stdoutmutex,fila_de_mesas,fila_de_posicao,0)
        posicoes.append(thread)
        thread.start()
    
    fotografos = []
    
    for j in range(4):
        thread = Fotografo.Fotografo(stdoutmutex, fila_de_posicao, 0)
        fotografos.append(thread)
        thread.start()
    
    print('Saindo da Thread principal.')



