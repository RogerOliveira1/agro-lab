import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class DiagnosticoCalopsitaService:
    def __init__(self, dataset_path='./datasets/hemograma_calopsitas.csv'):
        self.resultados_regressao = {
            1: "Infecção Bacteriana",
            2: "Infecção Viral",
            3: "Infecção Parasitária",
            4: "Intoxicação",
            5: "Desnutrição",
            6: "Doença Hepática",
            7: "Doença Renal",
            8: "Anemia Hemolítica",
            9: "Estresse Crônico",
            10: "Infecção Fúngica",
            11: "Neoplasia",
            12: "Inflamação Crônica"
        }

        dados = pd.read_csv(dataset_path)
        dados = dados.fillna(dados.mean())
        dados.replace([np.inf, -np.inf], np.nan, inplace=True)
        dados.dropna(inplace=True)

        x = dados[['Eritrocitos', 'Hemoglobina', 'Hematocrito', 'HCM', 'VGM', 'CHGM',
                   'Metarrubricitos', 'ProteinaPlasmatica', 'Leucocitos', 'Leucograma',
                   'Segmentados', 'Bastonetes', 'Blastos', 'Metamielocitos', 'Mielocitos',
                   'Linfocitos', 'Monocitos', 'Eosinofilos', 'Basofilos', 'Plaquetas']]
        y = dados['Diagnostico']

        self.model = LinearRegression().fit(x, y)

    def prever(self, data: dict):
        features = np.array([[
            data['Eritrocitos'], data['Hemoglobina'], data['Hematocrito'], data['HCM'],
            data['VGM'], data['CHGM'], data['Metarrubricitos'], data['ProteinaPlasmatica'],
            data['Leucocitos'], data['Leucograma'], data['Segmentados'], data['Bastonetes'],
            data['Blastos'], data['Metamielocitos'], data['Mielocitos'], data['Linfocitos'],
            data['Monocitos'], data['Eosinofilos'], data['Basofilos'], data['Plaquetas']
        ]])

        predicted = self.model.predict(features)[0]
        codigo = int(predicted)
        nome = self.resultados_regressao.get(codigo, "Doença Desconhecida")
        return round(predicted, 1), nome
