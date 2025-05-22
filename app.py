from flask import Flask, request, jsonify
from services.diagnosticos.diagnostico_cachorro_service import DiagnosticoCachorroService
from services.diagnosticos.diagnostico_calopsita_service import DiagnosticoCalopsitaService
from services.diagnosticos.diagnostico_ovinos_service import DiagnosticoOvinosService

app = Flask(__name__)
serviceCachorro = DiagnosticoCachorroService()
serviceCalopsita = DiagnosticoCalopsitaService()
serviceOvinos = DiagnosticoOvinosService()

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

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)