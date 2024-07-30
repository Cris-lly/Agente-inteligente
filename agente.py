from mundo import Mundo, random
class Agente:
    def __init__(self, mundo, pontuacao = 0 ,bateria = 50):
        self.bateria = bateria
        self.pos = [0,0]
        self.pontuacao = pontuacao
        self.memoria = 0
        self.ultima_cond = ''
        self.acabou = False
        self.log = f"CONSEQUENCIA, PONTOS GANHOS, BATERIA PERDIDA, PONTOS ATUAIS, BATERIA ATUAL, QTD SUJEIRA\n"
        self.mundo = mundo

    def _verificar_ultima_acao(self,):
        if self._aux_verificar_ultima_acao('esq'):
            return 'mover_esquerda'
        if self._aux_verificar_ultima_acao('dir'):
            return 'mover_direita'
        if self._aux_verificar_ultima_acao('baixo'):
            return 'mover_baixo'
        if self._aux_verificar_ultima_acao('cima'):
            return 'mover_cima'
    
    def _aux_verificar_ultima_acao(self, pos):
        return pos in self.ultima_cond
    
    def _verificar_bateu(self,):
        return 'parede' in self.ultima_cond
    
    def _oposto_acao(self, acao):
        pass
            
    def mover_esquerda(self):
        if self.pos[1] - 1 < 0:
            self.pontuacao -= 1
            self.bateria -=1
            suj_atual = self.mundo.qtd_sujeira()
            self.ultima_cond = f'esq - Bateu na parede, {-1}, {-1},{self.pontuacao},{self.bateria}, {suj_atual}\n'
            self.log += self.ultima_cond #estado, pontos, bateria, pontos atuais, bateria atual
        else:
            self.pos[1] -= 1 
            self.bateria -=1
            self.pontuacao += 1
            suj_atual = self.mundo.qtd_sujeira()
            self.ultima_cond = f'Andou para a esq, {+1}, {-1},{self.pontuacao},{self.bateria}, {suj_atual}\n'
            self.log += self.ultima_cond
            
    def mover_direita(self):
        if self.pos[1] + 1 >= self.mundo.colunas:
            self.pontuacao -= 1
            self.bateria -=1
            suj_atual = self.mundo.qtd_sujeira()
            self.ultima_cond = f'dir - Bateu na parede, {-1}, {-1},{self.pontuacao},{self.bateria}, {suj_atual}\n'
            self.log += self.ultima_cond #estado, pontos, bateria, pontos atuais, bateria atual
        else:
            self.pos[1] += 1 
            self.bateria -=1
            self.pontuacao += 1
            suj_atual = self.mundo.qtd_sujeira()
            self.ultima_cond = f'Andou para a dir, {+1}, {-1},{self.pontuacao},{self.bateria}, {suj_atual}\n'
            self.log += self.ultima_cond
    
    def mover_baixo(self):
        if self.pos[0] + 1 >= self.mundo.colunas:
            self.pontuacao -= 1
            self.bateria -=1
            suj_atual = self.mundo.qtd_sujeira()
            self.ultima_cond = f'baixo - Bateu na parede, {-1}, {-1},{self.pontuacao},{self.bateria}, {suj_atual}\n'
            self.log += self.ultima_cond #estado, pontos, bateria, pontos atuais, bateria atual
        else:
            self.pos[0] += 1 
            self.bateria -=1
            self.pontuacao += 1
            suj_atual = self.mundo.qtd_sujeira()
            self.ultima_cond = f'Andou para a baixo, {+1}, {-1},{self.pontuacao},{self.bateria}, {suj_atual}\n'
            self.log += self.ultima_cond
        
    
    def mover_cima(self):
        if self.pos[0] - 1 < 0:
            self.pontuacao -= 1
            self.bateria -=1
            suj_atual = self.mundo.qtd_sujeira()
            self.ultima_cond = f'cima - Bateu na parede, {-1}, {-1},{self.pontuacao},{self.bateria}, {suj_atual}\n'
            self.log += self.ultima_cond #estado, pontos, bateria, pontos atuais, bateria atual
        else:
            self.pos[0] -= 1 
            self.bateria -=1
            self.pontuacao += 1
            suj_atual = self.mundo.qtd_sujeira()
            self.ultima_cond = f'Andou para a cima, {+1}, {-1},{self.pontuacao},{self.bateria}, {suj_atual}\n'
            self.log += self.ultima_cond
    
    #só uma funcao auxiliar pra testar se ta fzndo tudo direito
    def ver(self):
        return self.pos
        #print(self.mundo.mundo[self.pos[0], self.pos[1]])
    
    def limpar(self):
        x = self.pos[0]
        y = self.pos[1]
        if self.mundo.mundo[x][y]==True:
            self.mundo.mundo[x][y]=False
            
    def __aux_mov(self, acao):
        if acao == 'mover_baixo':
            self.mover_baixo()
        elif acao == 'mover_cima':
            self.mover_cima()
        elif acao == 'mover_esquerda':
            self.mover_esquerda()
        else:
            self.mover_direita()
        
    def __aux_buscar_pos(self, pos):
        for dicionario in self.memoria:
            if dicionario["pos"] == pos:
                return dicionario
        return None
    
    def __aux_add_dict(self, pos):
        return {"pos": pos,
                "esq": None,
                "dir": None,
                "cima": None,
                "baixo": None}
    
    def verifica_bateria(self,):
        if self.bateria <= 0:
            self.acabou = True
            raise Exception("Bateria acabou")
            
    def limpar_reativo_simples(self):
        lista_acoes = ['mover_baixo', 'mover_cima', 'mover_esquerda','mover_direita']
        sorteio = random.randint(0,3)
        acao = lista_acoes[sorteio]
        #print(acao)
        self.limpar()
        self.__aux_mov(acao)
        self.limpar()
        #print(self.pos)
        #print(self.ver())
    # 431 4x4
    
    def caracol_vertical(self,):
        self.limpar()
        self.__aux_mov('mover_direita')
        self.limpar()
        self.verifica_bateria()
        if self._verificar_bateu():
            return
        while not self._verificar_bateu():
            for _ in range (self.memoria-1):
                self.limpar()
                self.__aux_mov('mover_cima')
                self.limpar()
                self.verifica_bateria()
            self.limpar()
            self.__aux_mov('mover_direita')
            self.limpar()
            if self._verificar_bateu():
                break
            for _ in range (self.memoria-1):
                self.limpar()
                self.__aux_mov('mover_baixo')
                self.limpar()
                self.verifica_bateria()
            self.limpar()
            self.__aux_mov('mover_direita')
            self.limpar()
            self.verifica_bateria()
            if self._verificar_bateu():
                break 
    
    def caracol_horizontal(self,):
        self.limpar()
        self.__aux_mov('mover_baixo')
        self.limpar()
        self.verifica_bateria()
        if self._verificar_bateu():
            return
        while not self._verificar_bateu():
            for _ in range (self.memoria-1):
                self.limpar()
                self.__aux_mov('mover_esquerda')
                self.limpar()
                self.verifica_bateria()
            self.limpar()
            self.__aux_mov('mover_baixo')
            self.limpar()
            if self._verificar_bateu():
                break
            for _ in range (self.memoria-1):
                self.limpar()
                self.__aux_mov('mover_direita')
                self.limpar()
                self.verifica_bateria()
            self.limpar()
            self.__aux_mov('mover_baixo')
            self.limpar()
            self.verifica_bateria()
            if self._verificar_bateu():
                break        
       

    def repetir_ate_nao_bater(self, acao, acao_proibida, lista_acoes):
        if self._verificar_bateu():
                while self._verificar_bateu():
                    acao_proibida.append(acao)
                    while True:
                        acao=random.choice(lista_acoes)
                        if acao not in acao_proibida:
                            break
                    self.limpar()
                    self.__aux_mov(acao)
                    self.limpar()
                    self.verifica_bateria()
                    self.limpar()
    
    def limpar_reativo_modelo(self):
        acao_proibida = []
        lista_acoes = ['mover_baixo', 'mover_cima', 'mover_esquerda','mover_direita']
        try:
            if self.memoria == 0:
                acao = random.choice(lista_acoes)
                self.limpar()
                self.__aux_mov(acao)
                self.limpar()
                self.verifica_bateria()
                self.repetir_ate_nao_bater(acao, acao_proibida, lista_acoes)
                self.memoria +=1
            else:
                ultima = self._verificar_ultima_acao()
                while not self._verificar_bateu():
                    self.limpar()
                    self.__aux_mov(ultima)
                    self.limpar()
                    self.verifica_bateria()
                    self.memoria+=1
                if ultima == 'mover_baixo':
                    self.caracol_vertical()
                elif ultima == 'mover_direita':
                    self.caracol_horizontal()
                self.acabou = True
        except Exception as e:
            print(e)
            return
                
                    
    
    
    
    
    
    
    
    '''  
    #random.seed(1)
    def limpar_reativo_modelo(self):
        if self.memoria == None:
            movs = 0
            lista_acoes = ['mover_baixo', 'mover_cima', 'mover_esquerda','mover_direita']
            acao = random.choice(lista_acoes)
            self.limpar()
            self.__aux_mov(acao)
            if self._verificar_bateu():
                acao_excluir = []
                while self._verificar_bateu():
                    acao_excluir.append(acao)
                    while True:
                        acao = random.choice(lista_acoes)
                        if acao not in acao_excluir:
                            break
                    self.__aux_mov(acao)
                    self.limpar()
            else:
                movs +=1
                while not self._verificar_bateu():
                    self.limpar()
                    self.__aux_mov(acao)
                    movs+=1
                self.memoria = movs
        else:
            acao = self._verificar_ultima_acao()
            if acao == 'mover_direita':
                self.__aux_mov('mover_baixo')
                self.limpar
                for _ in range (self.memoria-1):
                    self.limpar()
                    self.__aux_mov('mover_esquerda')
            if acao == 'mover_esquerda':
                self.__aux_mov('mover_baixo')
                self.limpar
                for _ in range (self.memoria-1):
                    self.limpar()
                    self.__aux_mov('mover_direita')
            
            
        
    
    
    
    
    
    
    
    
    
    
      
    def limpar_reativo_modelo(self):
        lista_acoes = ['mover_baixo', 'mover_cima', 'mover_esquerda','mover_direita']
        acao = random.choice(lista_acoes)
        print(acao)
        self.limpar()
        self.__aux_mov(acao)
        self.limpar()
        if not self._verificar_bateu():
            while not self._verificar_bateu():
                self.limpar()
                self.__aux_mov(acao)
                self.limpar()
            if self._verificar_ultima_pos('dir'):
                
        else:
            while self._verificar_bateu():
                lista_acoes.remove(acao)
                acao = random.choice(lista_acoes)
                self.limpar()
                self.__aux_mov(acao)
                self.limpar()
            '''
                
        
               