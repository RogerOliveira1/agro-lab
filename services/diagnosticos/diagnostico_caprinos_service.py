import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class DiagnosticoCaprinoService:
    def __init__(self, dataset_path='./datasets/dataset-caprinos.csv'):
        self.resultados_regressao = {
            1: "Ectima Contagioso",
            2: "Linfonodose Caseosa",
            3: "Brucelose Caprina",
            4: "Artrite Encefalite Caprina (CAE)",
            5: "Paratuberculose",
            6: "Mastite Caprina",
            7: "Toxemia da Prenhez",
            8: "Coccidiose",
            9: "Pneumonia",
            10: "Gastroenterite Parasitária",
            11: "Enterotoxemia",
            12: "Deficiência de Cobre",
            13: "Hipocalcemia",
            14: "Tripanossomose",
            15: "Contaminação por Carbúnculo",
            16: "Pododermatite",
            17: "Hepatopatia Crônica",
            18: "Anemia Infecciosa",
            19: "Infecção Bacteriana Sistêmica"
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
