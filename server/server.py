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

# app instance
app = Flask(__name__)
CORS(app)

# Função para criar a tabela e adicionar dados
def criar_tabela_e_adicionar_dados():
    # Conectar ao banco de dados (ou criar se não existir)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Criar a tabela se ainda não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS criptos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            votos INTEGER
        )
    ''')

    # Adicionar dados na tabela
    criptos = [
        {'id': 1, 'nome': 'Bitcoin', 'votos': 100},
        {'id': 2, 'nome': 'Ethereum', 'votos': 50},
        {'id': 3, 'nome': 'Polkadot', 'votos': 25},
        {'id': 4, 'nome': 'Solana', 'votos': 10},
        {'id': 5, 'nome': 'Dogecoin', 'votos': 99},
        {'id': 6, 'nome': 'Cardano', 'votos': 5},
        {'id': 7, 'nome': 'BNB', 'votos': 30},
        {'id': 8, 'nome': 'Litecoin', 'votos': 15},
        {'id': 9, 'nome': 'Chainlink', 'votos': 45},
        {'id': 10, 'nome': 'Wrapped Bitcoin', 'votos': 20}
    ]

    # iteração para INSERIR os vlores na tabela criptos
    for cripto in criptos:
        cursor.execute('''
            INSERT OR IGNORE INTO criptos (id, nome, votos)
            VALUES (?, ?, ?)
        ''', (cripto['id'], cripto['nome'], cripto['votos']))

    # Commit para salvar as alterações
    conn.commit()

    # Fechar a conexão
    conn.close()

# Chamar a função para criar a tabela e adicionar dados
criar_tabela_e_adicionar_dados()

# Função para listar todas as criptos do banco de dados
@app.route('/criptos/', methods=['GET'])
def listar_criptos():
    # Conectar ao banco de dados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Executar a consulta para obter todos os registros da tabela criptos
    cursor.execute('''
        SELECT * FROM criptos
    ''')

    # Buscar todos os resultados da consulta
    criptos_from_db = cursor.fetchall()

    # Fechar a conexão
    conn.close()

    # Transformar os resultados em uma lista de dicionários
    criptos_list = [{'id': row[0], 'nome': row[1], 'votos': row[2]} for row in criptos_from_db]

    # Retornar os dados como resposta JSON
    return jsonify(criptos_list)

# Função para adicionar um voto pelo ID no banco de dados
@app.route('/criptos/votar/<int:id>', methods=['POST'])
def adicionar_voto(id):
    # Conectar ao banco de dados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Verificar se o ID existe na tabela criptos
    cursor.execute('''
        SELECT * FROM criptos WHERE id = ?
    ''', (id,))

    cripto = cursor.fetchone()

    if cripto is not None:
        # Atualizar o número de votos no banco de dados
        cursor.execute('''
            UPDATE criptos
            SET votos = votos + 1
            WHERE id = ?
        ''', (id,))

        # Commit para salvar as alterações
        conn.commit()

        # Fechar a conexão
        conn.close()

        # Retornar o número de votos atualizado
        return jsonify({'votos': cripto[2] + 1})
    else:
        # ID não encontrado
        return jsonify({'error': 'ID não encontrado'}), 404



if __name__ == "__main__":
    # inicia o server aceitando requisições http
    app.run()
