import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class DiagnosticoBovinosService:
    def __init__(self, dataset_path='./datasets/dataset-bovinos.csv'):
        self.resultados_regressao = {
            1: "Mastite",
            2: "Febre Aftosa",
            3: "Brucelose",
            4: "Tuberculose",
            5: "Diarreia Viral Bovina (BVD)",
            6: "Leptospirose",
            7: "Carbúnculo Sintomático",
            8: "Botulismo",
            9: "Raiva",
            10: "Tricomonose",
            11: "Neosporose",
            12: "Cetose",
            13: "Hipocalcemia (Febre do Leite)",
            14: "Acidose Ruminal",
            15: "Dermatofilose",
            16: "Pneumonia",
            17: "Retenção de Placenta",
            18: "Timpanismo",
            19: "Parasitismo Gastrointestinal"
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
