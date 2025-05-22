import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class DiagnosticoEquinoService:
    def __init__(self, dataset_path='./datasets/dataset-equinos.csv'):
        self.resultados_regressao = {
            1: "Anemia Infecciosa Equina",
            2: "Mormo",
            3: "Encefalomielite",
            4: "Raiva",
            5: "Tétano",
            6: "Leptospirose",
            7: "Doença do Carrapato",
            8: "Infecção Respiratória",
            9: "Cólicas Intestinais",
            10: "Miopatia Nutricional",
            11: "Hepatopatia",
            12: "Neoplasia Hematológica",
            13: "Endometrite",
            14: "Pneumonia",
            15: "Babesiose",
            16: "Artrite Séptica",
            17: "Hemorragia Interna",
            18: "Linfangite",
            19: "Dermatite Fúngica"
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
