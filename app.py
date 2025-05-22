from flask import Flask, request, jsonify
from services.diagnosticos.diagnostico_bovinos_service import DiagnosticoBovinosService
from services.diagnosticos.diagnostico_cachorro_service import DiagnosticoCachorroService
from services.diagnosticos.diagnostico_calopsita_service import DiagnosticoCalopsitaService
from services.diagnosticos.diagnostico_caprinos_service import DiagnosticoCaprinoService
from services.diagnosticos.diagnostico_equinos_service import DiagnosticoEquinoService
from services.diagnosticos.diagnostico_ovinos_service import DiagnosticoOvinosService
from services.diagnosticos.diagnostico_suinos_service import DiagnosticoSuinoService
from services.diagnosticos.diagnostico_tartaruga_service import DiagnosticoTartarugaService

app = Flask(__name__)
serviceCachorro = DiagnosticoCachorroService()
serviceCalopsita = DiagnosticoCalopsitaService()
serviceOvinos = DiagnosticoOvinosService()
serviceBovinos = DiagnosticoBovinosService()
serviceCaprino = DiagnosticoCaprinoService()
serviceEquino = DiagnosticoEquinoService()
serviceSuino = DiagnosticoSuinoService()
serviceTartaruga = DiagnosticoTartarugaService()

@app.route('/diagnostico/cao', methods=['POST'])
def prever_diagnostico_cao():
    data = request.json
    previsao, nome_doenca = serviceCachorro.prever(data)

    print(f"Previsão numérica: {previsao}")
    print(f"Doença identificada: {nome_doenca}")

    return jsonify({
        'prever_diagnostico': previsao,
        'nome_da_doenca': nome_doenca
    })

@app.route('/diagnostico/calopsita', methods=['POST'])
def prever_diagnostico_calopsita():
    data = request.json
    previsao, nome_doenca = serviceCalopsita.prever(data)

    print(f"Previsão numérica: {previsao}")
    print(f"Doença identificada: {nome_doenca}")

    return jsonify({
        'prever_diagnostico': previsao,
        'nome_da_doenca': nome_doenca
    })
    
@app.route('/diagnostico/ovinos', methods=['POST'])
def prever_diagnostico_ovinos():
    data = request.json
    previsao, nome_doenca = serviceOvinos.prever(data)

    print(f"Previsão numérica: {previsao}")
    print(f"Doença identificada: {nome_doenca}")

    return jsonify({
        'prever_diagnostico': previsao,
        'nome_da_doenca': nome_doenca
    })

@app.route('/diagnostico/bovinos', methods=['POST'])
def prever_diagnostico_bovinos():
    data = request.json
    previsao, nome_doenca = serviceBovinos.prever(data)

    print(f"Previsão numérica: {previsao}")
    print(f"Doença identificada: {nome_doenca}")

    return jsonify({
        'prever_diagnostico': previsao,
        'nome_da_doenca': nome_doenca
    })            

@app.route('/diagnostico/caprinos', methods=['POST'])
def prever_diagnostico_caprinos():
    data = request.json
    previsao, nome_doenca = serviceCaprino.prever(data)

    print(f"Previsão numérica: {previsao}")
    print(f"Doença identificada: {nome_doenca}")

    return jsonify({
        'prever_diagnostico': previsao,
        'nome_da_doenca': nome_doenca
    })

@app.route('/diagnostico/equinos', methods=['POST'])
def prever_diagnostico_equinos():
    data = request.json
    previsao, nome_doenca = serviceEquino.prever(data)

    print(f"Previsão numérica: {previsao}")
    print(f"Doença identificada: {nome_doenca}")

    return jsonify({
        'prever_diagnostico': previsao,
        'nome_da_doenca': nome_doenca
    })

@app.route('/diagnostico/suinos', methods=['POST'])
def prever_diagnostico_suinos():
    data = request.json
    previsao, nome_doenca = serviceSuino.prever(data)

    print(f"Previsão numérica: {previsao}")
    print(f"Doença identificada: {nome_doenca}")

    return jsonify({
        'prever_diagnostico': previsao,
        'nome_da_doenca': nome_doenca
    })

@app.route('/diagnostico/tartaruga', methods=['POST'])
def prever_diagnostico_tartaruga():
    data = request.json
    previsao, nome_doenca = serviceTartaruga.prever(data)

    print(f"Previsão numérica: {previsao}")
    print(f"Doença identificada: {nome_doenca}")

    return jsonify({
        'prever_diagnostico': previsao,
        'nome_da_doenca': nome_doenca
    })

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)