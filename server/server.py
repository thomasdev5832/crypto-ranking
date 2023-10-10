from flask import Flask, jsonify, request
from flask_cors import CORS

# Importa o modulo do SQLite
import sqlite3

# Conecta ao banco de dados (ou cria um novo banco de dados se ele não existir)
conn = sqlite3.connect('database.db')

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Cria uma tabela para armazenar os dados
cursor.execute('''
    CREATE TABLE IF NOT EXISTS criptos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        votos INTEGER
    )
''')

# Função para inserir um novo dado no banco de dados
def gravar_cripto(id, nome, votos):
    cursor.execute('''
        INSERT INTO criptos (id, nome, votos)
        VALUES (?, ?, ?)
    ''', (id, nome, votos))
    conn.commit()

# Função para recuperar todos os dados do banco de dados
def obter_criptos():
    cursor.execute('''
        SELECT * FROM criptos
    ''')
    return cursor.fetchall()

def adicionar_voto_por_id(id):
    cursor.execute('''
        UPDATE dados
        SET votos = votos + 1
        WHERE id = ?
    ''', (id,))
    conn.commit()

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



# Listar todas criptos
@app.route('/criptos/', methods=['GET'])
def listar_criptos():
    return jsonify(criptos)

# Adicionar um voto pelo ID
@app.route('/criptos/votar/<int:id>', methods=['POST'])
def adicionar_voto(id):
    for cripto in criptos:
        if cripto.get('id') == id:
            cripto['votos'] += 1
            return jsonify(cripto['votos'])

# consultar cripto pelo ID
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
