from flask import Flask, jsonify
from flask_cors import CORS

# app instance
app = Flask(__name__)
CORS(app)

# app route to home
# methods=['GET'] -> aceita apenas método GET
# retorna um json
@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "Qual sua crypto favorita?",
        'cryptos': ['Bitcoin', 'Ethereum', 'Polkadot', 'Cardano', 'Solana', 'Dogecoin']
    })

if __name__ == "__main__":
    # inicia o server aceitando requisições http
    app.run(debug=True, port=8080)
