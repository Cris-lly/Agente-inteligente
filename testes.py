if __name__ == "__main__":
    mundo = Mundo(linhas= 10, colunas= 10)
    print(mundo)
    x = Agente(mundo = mundo)
    mundo.constroiMundo()
    print(x.pos)
    #x.mover_direita()
    x.mover_esquerda()
    print(x.log)        