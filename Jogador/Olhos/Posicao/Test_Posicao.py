import unittest
import threading, queue
from Posicao import Posicao

class Test_Posicao(unittest.TestCase):

    def test_run(self):
        # Vamos criar duas filas 
        queue_de_leitura = queue.Queue() # Fila de leitura 
        queue_de_escrita = queue.Queue() # Fila de escrita 

        # Vamos adicionar três 'dicionarios' na Queue leitura
        queue_de_leitura.put({'Titulo da Janela':'Exemplo 1 - Bloco de notas'})
        queue_de_leitura.put({'Titulo da Janela':'Exemplo 2 - Bloco de notas'})

        # Vamos criar uma mutex 
        stdoutmutex = threading.Lock()

        threads = []

        # Vamos criar uma Thread para ler a queue de leitura e escrever na queue de escrita
        for i in range(2):
            thread = Posicao(stdoutmutex,queue_de_leitura,queue_de_escrita,0)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        
        a = queue_de_escrita.get(block=False)
        b = {'Titulo da Janela':'Exemplo 1 - Bloco de notas','posicao X':0,'posicao Y':0}
        self.assertEqual(a, b)

        a = queue_de_escrita.get(block=False)
        b = {'Titulo da Janela':'Exemplo 2 - Bloco de notas','posicao X':0,'posicao Y':0}
        self.assertEqual(a, b)

if __name__ == "__main__":   
    unittest.main()

        
