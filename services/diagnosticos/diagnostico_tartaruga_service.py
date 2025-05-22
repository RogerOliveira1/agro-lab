import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class DiagnosticoTartarugaService:
    def __init__(self, dataset_path='./datasets/dataset-tartaruga-tigre.csv'):
        self.resultados_regressao = {
            1: "Pneumonia",
            2: "Micoses Cutâneas",
            3: "Doença Óssea Metabólica",
            4: "Hipovitaminose A",
            5: "Septicemia",
            6: "Infecção por Salmonella",
            7: "Desidratação Grave",
            8: "Hepatopatia",
            9: "Prolapso Cloacal",
            10: "Infecção de Carapaça",
            11: "Cegueira Nutricional",
            12: "Infecção Bacteriana Sistêmica",
            13: "Parasitas Gastrointestinais",
            14: "Deficiência de Cálcio",
            15: "Pododermatite",
            16: "Doença Fúngica Sistêmica",
            17: "Abcessos",
            18: "Infecção Respiratória Crônica",
            19: "Intoxicação Alimentar"
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
