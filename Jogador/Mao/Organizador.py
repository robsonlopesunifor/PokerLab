
import pyautogui


class Organizador:

        def __init__(self,palavra_chave,divisoes):
                lista_de_janelas_com_a_palavra_chave_no_titulo = self.retornar_lista_de_janelas_com_a_palavra_chave_no_titulo(palavra_chave)
                self.organizar_as_janelas(divisoes, lista_de_janelas_com_a_palavra_chave_no_titulo)

        def retornar_lista_de_janelas_com_a_palavra_chave_no_titulo(self,palavra_chave):
                dicionario_de_janelas = pyautogui.getWindows()
                lista_de_janelas_com_a_palavra_chave = []
                
                for item in dicionario_de_janelas:
                        if item.find(palavra_chave) != -1:
                                lista_de_janelas_com_a_palavra_chave.append(item)
                return lista_de_janelas_com_a_palavra_chave

        def organizar_as_janelas(self,numero_de_divisoes_da_tela,lista_de_janelas):
                tamanho_da_tela = pyautogui.size()
                conjunto_de_informacoes_das_janelas = []
                
                largura_da_janela = int(tamanho_da_tela[0]/numero_de_divisoes_da_tela) 
                altura_da_janela = int(tamanho_da_tela[1]/numero_de_divisoes_da_tela)

                for idx,item in enumerate(lista_de_janelas):
                
                        posicao_x_da_janela_na_tela = (largura_da_janela - 15 )* int((idx) / numero_de_divisoes_da_tela)
                        posicao_y_da_janela_na_tela = (altura_da_janela - 10 )* ((idx) % numero_de_divisoes_da_tela)

                        pyautogui.getWindow(item).resize(largura_da_janela, altura_da_janela)
                        pyautogui.getWindow(item).move(posicao_x_da_janela_na_tela,posicao_y_da_janela_na_tela)

                        informacoes_da_janela = {'titulo':item,
                                                 'dimencao':(largura_da_janela,altura_da_janela),
                                                 'posicao':(posicao_x_da_janela_na_tela,posicao_y_da_janela_na_tela)}

                        conjunto_de_informacoes_das_janelas.append(informacoes_da_janela)
                        
                return print(conjunto_de_informacoes_das_janelas)

        


organizador = Organizador('Bloco de notas',3)




       
    
    
    
    

    

    
    
    
