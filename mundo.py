import numpy as np
import json
import random
#random.seed(42)

class Mundo:
    def __init__(self, linhas, colunas, estado=False, mundo=0):
        self.linhas = linhas
        self.colunas = colunas
        self.estado = estado
        self.mundo = mundo
    
    def importar_mundo(self, filename):
        with open(filename, 'r') as f:
            matriz_lista_de_json = json.load(f)
        self.mundo = np.array(matriz_lista_de_json, dtype=bool)
        
            
    def constroiMundo(self):
        self.mundo = np.full((self.linhas, self.colunas), self.estado, dtype=bool)
        #print(self.mundo)
        self.sujaMundo()
        print(self.mundo)
        #print(self.mundo[0,0])
        #print(self.mundo[1,1])
    def sujaMundo(self):
        for coluna in range(1, self.colunas):
            for linha in range(1, self.linhas):

                # gerando se o local está limpo ou sujo:
                local = random.choice([True, False])
                
                if local == True:
                    self.mundo[coluna, linha] = local

    def obterPosicao(self):
        return (self.linhas, self.colunas)

    def printar_mundo(self):
        print(self.mundo)
        
    def qtd_sujeira(self):
        qtd_suj = np.count_nonzero(self.mundo)
        return qtd_suj


