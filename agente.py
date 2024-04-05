from mundo import Mundo, random

class Agente:
    def __init__(self, mundo, pontuacao = 0 ,bateria = 50):
        self.bateria = bateria
        self.pos = [0,0]
        self.pontuacao = pontuacao
        self.memoria = []
        self.log = f"CONSEQUENCIA, PONTOS GANHOS, BATERIA PERDIDA, PONTOS ATUAIS, BATERIA ATUAL, QTD SUJEIRA\n"
        self.mundo = mundo
        
    def mover_esquerda(self):
        if self.pos[1] - 1 < 0:
            self.pontuacao -= 1
            self.bateria -=1
            suj_atual = self.mundo.qtd_sujeira()
            self.log += f'Esq - Bateu na parede, {-1}, {-1},{self.pontuacao},{self.bateria}, {suj_atual}\n' #estado, pontos, bateria, pontos atuais, bateria atual
        else:
            self.pos[1] -= 1 
            self.bateria -=1
            self.pontuacao += 1
            suj_atual = self.mundo.qtd_sujeira()
            self.log += f'Andou para a esquerda, {+1}, {-1},{self.pontuacao},{self.bateria}, {suj_atual}\n'
    
    def mover_direita(self):
        if self.pos[1] + 1 >= self.mundo.colunas:
            self.pontuacao -= 1
            self.bateria -=1
            suj_atual = self.mundo.qtd_sujeira()
            self.log += f'Dir - Bateu na parede,  {-1}, {-1},{self.pontuacao},{self.bateria}, {suj_atual}\n' #estado, pontos, bateria, pontos atuais, bateria atual
        else:
            self.pos[1] += 1 
            self.bateria -=1
            self.pontuacao += 1
            suj_atual = self.mundo.qtd_sujeira()
            self.log += f'Andou para a direita, {+1}, {-1},{self.pontuacao},{self.bateria}, {suj_atual}\n'
    
    def mover_baixo(self):
        if self.pos[0] + 1 >= self.mundo.colunas:
            self.pontuacao -= 1
            self.bateria -=1
            suj_atual = self.mundo.qtd_sujeira()
            self.log += f'Baixo - Bateu na parede,  {-1}, {-1},{self.pontuacao},{self.bateria}, {suj_atual}\n' #estado, pontos, bateria, pontos atuais, bateria atual
        else:
            self.pos[0] += 1 
            self.bateria -=1
            self.pontuacao += 1
            suj_atual = self.mundo.qtd_sujeira()
            self.log += f'Andou para baixo, {+1}, {-1}, {self.pontuacao}, {self.bateria}, {suj_atual}\n'
        
    
    def mover_cima(self):
        if self.pos[0] - 1 < 0:
            self.pontuacao -= 1
            self.bateria -=1
            suj_atual = self.mundo.qtd_sujeira()
            self.log += f'Cima - Bateu na parede,  {-1}, {-1},{self.pontuacao},{self.bateria}, {suj_atual}\n' #estado, pontos, bateria, pontos atuais, bateria atual
        else:
            self.pos[0] -= 1 
            self.bateria -=1
            self.pontuacao += 1
            suj_atual = self.mundo.qtd_sujeira()
            self.log += f'Andou para cima, {+1}, {-1},{self.pontuacao},{self.bateria}, {suj_atual}\n'
    
    #só uma funcao auxiliar pra testar se ta fzndo tudo direito
    def ver(self):
        return self.pos
        #print(self.mundo.mundo[self.pos[0], self.pos[1]])
    
    def limpar(self):
        x = self.pos[0]
        y = self.pos[1]
        if self.mundo.mundo[x][y]==True:
            self.mundo.mundo[x][y]=False
    
    def limpar_reativo_simples(self):
        lista_acoes = ['mover_baixo', 'mover_cima', 'mover_esquerda','mover_direita']
        sorteio = random.randint(0,3)
        acao = lista_acoes[sorteio]
        print(acao)
        self.limpar()
        if acao == 'mover_baixo':
            self.mover_baixo()
        elif acao == 'mover_cima':
            self.mover_cima()
        elif acao == 'mover_esquerda':
            self.mover_esquerda()
        else:
            self.mover_direita()
        self.limpar()
        #print(self.pos)
        print(self.ver())
        
               