from agente import Agente
from mundo import Mundo
from estatisticas import Stats

mundo = Mundo(3, 3)
mundo.importar_mundo("matriz_suja.json")
carga = 16
agente_reativo_simples = Agente(mundo, bateria=carga)

def teste_agente(agente):
    while agente.bateria > 0:
        agente.limpar_reativo_simples()
    #print(agente_reativo_simples.log)
    #print(mundo.printar_mundo())
    stats = Stats(agente=agente, mundo=mundo)
    
    df = stats.logs_to_df()
    df.to_excel(f'logs\dados_agente_simples_{carga}_cargas.xlsx', index=True)
    print(df)
    stats.pontosXbateria()
    stats.sujeiraXbateria()
    #print(df)

if __name__ == "__main__":
    #mundo.printar_mundo()
    teste_agente(agente_reativo_simples)
    mundo.printar_mundo()
    
    