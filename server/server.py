from flask import Flask, jsonify, request
from flask_cors import CORS

# app instance
app = Flask(__name__)
CORS(app)

criptos = [
    {
        'id': 1,
        'nome': 'Bitcoin',
        'votos': 100
    },
    {
        'id': 2,
        'nome': 'Ethereum',
        'votos': 50
    },
    {
        'id': 3,
        'nome': 'Polkadot',
        'votos': 20
    },
    {
        'id': 4,
        'nome': 'Solana',
        'votos': 10
    },
    {
        'id': 5,
        'nome': 'Dogecoin',
        'votos': 99
    },
    {
        'id': 6,
        'nome': 'Cardano',
        'votos': 9
    },
    {
        'id': 7,
        'nome': 'BNB',
        'votos': 37
    },
    {
        'id': 8,
        'nome': 'Litecoin',
        'votos': 17
    },
    {
        'id': 9,
        'nome': 'Chainlink',
        'votos': 21
    },
    {
        'id': 10,
        'nome': 'Wrapped Bitcoin',
        'votos': 13
    }
]

# app route to home
# methods=['GET'] -> aceita apenas método GET
# retorna um json
@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "Qual sua crypto favorita?",
        'cryptos': ['Bitcoin', 'Ethereum', 'Polkadot', 'Cardano', 'Solana', 'Dogecoin']
    })

# Listar todas criptos
@app.route('/', methods=['GET'])
def listar_criptos():
    return jsonify(criptos)


# consultar (id)
@app.route('/criptos/<int:id>', methods=['GET'])
def obter_cripto_por_id(id):
    for cripto in criptos:
        if cripto.get('id') == id:
            return jsonify(cripto)

# editar (id)
@app.route('/criptos/<int:id>', methods=['PUT'])
def editar_cripto_por_id(id):
    # request.get_json() -> retorna as informações que foram enviadas do usuario para API
    cripto_alterada = request.get_json()
    # necessario saber o indice e o id da cripto a ser alterada
    # iterar 
    for indice, cripto in enumerate(criptos):
        if cripto.get('id') == id:
            criptos[indice].update(cripto_alterada)
            return jsonify(criptos[indice])


if __name__ == "__main__":
    # inicia o server aceitando requisições http
    app.run(debug=True, port=8080)
