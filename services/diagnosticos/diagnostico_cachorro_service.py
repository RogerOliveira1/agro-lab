import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class DiagnosticoCachorroService:
    def __init__(self, dataset_path='./datasets/dataset-hemograma.csv'):
        self.resultados_regressao = {
            1: "DRC", 2: "Hipercolesterolemia", 3: "Animia", 4: "Lesao Hepatica",
            5: "Infeccao Bacteriana", 6: "Desidratacao", 7: "Infeccao Parasitaria",
            8: "Infeccao Viral", 9: "DRC e Cardiopatia", 10: "Neoplasia hepatica",
            11: "Animia Hemolitica", 12: "Diabetes", 13: "Pre-Diabetes",
            14: "Animia e Infeccao", 15: "Hepatopata", 16: "Trombocitopenia e Inflamacao",
            17: "Hipoplasia Mieloide", 18: "Pancreatite", 19: "Inflamacao Grave"
        }

        dados = pd.read_csv(dataset_path)
        dados = dados.fillna(dados.mean())
        dados.replace([np.inf, -np.inf], np.nan, inplace=True)
        dados.dropna(inplace=True)

        x = dados[['Eritrocitos', 'Hemoglobina', 'Hematocrito','HCM', 'VGM', 'CHGM',
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
