import mundo
import agente
teste = mundo.Mundo(3, 3)
teste.constroiMundo()
agente_reativo_simples = agente.Agente(teste, bateria=10)

if __name__ == "__main__":
    #print(teste.printar_mundo())
    while agente_reativo_simples.bateria > 0:
        agente_reativo_simples.limpar_reativo_simples()
    print(agente_reativo_simples.log)
    print(teste.printar_mundo())
    