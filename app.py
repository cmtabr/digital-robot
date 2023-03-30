from flask import Flask, request, jsonify, render_template, redirect
import sqlite3

app = Flask(__name__)

DATABASE = 'database.db'

# Função para conectar com o banco de dados
def get_db():
    return sqlite3.connect(DATABASE)

# Função para fechar a conexão com o banco de dados
def close_db(conn):
    conn.close()

# Função para executar uma query no banco de dados
def execute_query(query, args=(), commit=False):
    conn = get_db()
    with conn:
        cursor = conn.cursor()
        cursor.execute(query, args)
        if commit:
            conn.commit()
        return cursor

# Rota principal, que exibe a última linha da tabela 'axis'
@app.route('/')
def index():
    query = 'SELECT id, x, y, z, r FROM axis ORDER BY id DESC LIMIT 1'
    last_entry = execute_query(query).fetchone()
    x, y, z, r = last_entry[1:]
    return render_template('index.html', x=x, y=y, z=z, r=r)

# Rota para receber os dados do formulário via POST e inseri-los na tabela 'axis'
@app.route('/data', methods=['POST'])
def post():
    query = 'INSERT INTO axis (x, y, z, r) VALUES (?, ?, ?, ?)'
    args = (request.form['x'], request.form['y'], request.form['z'], request.form['r'])
    execute_query(query, args, commit=True)
    return redirect('/')

# Rota para retornar a última linha da tabela 'axis' como um objeto JSON
@app.route('/data', methods=['GET'])
def get():
    query = 'SELECT id, x, y, z, r FROM axis ORDER BY id DESC LIMIT 1'
    last_entry = execute_query(query).fetchone()
    response = {'id': last_entry[0], 'x': last_entry[1], 'y': last_entry[2], 'z': last_entry[3], 'r': last_entry[4]}
    return jsonify(response)

# Executa o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)