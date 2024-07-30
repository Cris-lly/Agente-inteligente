import pandas as pd
from agente import Agente
from mundo import Mundo
from io import StringIO
import matplotlib.pyplot as plt

class Stats():
    def __init__(self, agente, mundo):
        self.agente = agente
        self.mundo = mundo
    
    def logs_to_df(self):
        obj_string = StringIO(self.agente.log)
        df = pd.read_csv(obj_string, sep = ',')
        #print(df)
        return df
    
    def pontosXbateria(self):
        df = self.logs_to_df()
        df_sorted = df.sort_values(by=' BATERIA ATUAL', ascending=False)
        plt.plot(df_sorted[' BATERIA ATUAL'], df_sorted[' PONTOS ATUAIS'], marker='o', linestyle='-')
        plt.title('Pontos Atuais em Função da Bateria Atual')
        plt.xlabel('Bateria Atual')
        plt.ylabel('Pontos Atuais')
        plt.grid(True)
        plt.gca().invert_xaxis()  # Inverter o eixo x para ordem decrescente
        plt.show()
        
    def sujeiraXbateria(self):
        df = self.logs_to_df()
        df_sorted = df.sort_values(by=' BATERIA ATUAL', ascending=False)
        plt.plot(df_sorted[' BATERIA ATUAL'], df_sorted[' QTD SUJEIRA'], marker='o', linestyle='-')
        plt.title('Bateria Atual em Função da Quantidade de Sujeira')
        plt.xlabel('Bateria Atual')
        plt.ylabel('Quantidade de Sujeira')
        plt.grid(True)
        plt.gca().invert_xaxis()
        plt.show()

