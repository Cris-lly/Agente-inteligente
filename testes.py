from agente import Agente
from mundo import Mundo
from estatisticas import Stats

teste = Mundo(10, 10)
teste.constroiMundo()
agente_reativo_simples = Agente(teste, bateria=1000)

if __name__ == "__main__":
    #print(teste.printar_mundo())
    while agente_reativo_simples.bateria > 0:
        agente_reativo_simples.limpar_reativo_simples()
    #print(agente_reativo_simples.log)
    #print(teste.printar_mundo())
    stats = Stats(agente=agente_reativo_simples, mundo=teste)
    stats.logs_to_df()
    stats.pontosXbateria()
    stats.sujeiraXbateria()
    