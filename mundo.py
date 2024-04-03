import numpy as np
import random


class Mundo:
    def __init__(self, linhas, colunas, estado=False, mundo=0):
        self.linhas = linhas
        self.colunas = colunas
        self.estado = estado
        self.mundo = mundo

    def constroiMundo(self):
        self.mundo = np.full((self.linhas, self.colunas), self.estado, dtype=bool)
        print(self.mundo)
        self.sujaMundo()
        print(self.mundo)

    def sujaMundo(self):
        for coluna in range(1, self.colunas):
            for linha in range(1, self.linhas):

                # gerando se o local está limpo ou sujo:
                local = random.choice([True, False])

                if local == True:
                    self.mundo[coluna, linha] = local

    def obterPosicao(self):
        return (self.linhas, self.colunas)



