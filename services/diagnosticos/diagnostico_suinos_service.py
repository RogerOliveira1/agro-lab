import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class DiagnosticoSuinoService:
    def __init__(self, dataset_path='./datasets/dataset-suinos.csv'):
        self.resultados_regressao = {
            1: "Doença de Glässer",
            2: "Peste Suína Clássica",
            3: "Peste Suína Africana",
            4: "Leptospirose",
            5: "Salmonelose",
            6: "Colibacilose",
            7: "Actinobacilose Suína",
            8: "Disenteria Suína",
            9: "Pneumonia Enzoótica",
            10: "Circovirose",
            11: "Parvovirose Suína",
            12: "Síndrome Reprodutiva e Respiratória dos Suínos (PRRS)",
            13: "Sarna Sarcóptica",
            14: "Cisticercose",
            15: "Hepatopatia Crônica",
            16: "Enteropatia Proliferativa",
            17: "Encefalomielite Suína",
            18: "Infecção Sistêmica Bacteriana",
            19: "Deficiência Nutricional Grave"
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
