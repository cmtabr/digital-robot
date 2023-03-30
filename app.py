from flask import Flask, request, jsonify, render_template, redirect
import sqlite3

app = Flask(__name__)

DATABASE = 'database.db'

def get_db():
    return sqlite3.connect(DATABASE)

def close_db(conn):
    conn.close()

def execute_query(query, args=(), commit=False):
    conn = get_db()
    with conn:
        cursor = conn.cursor()
        cursor.execute(query, args)
        if commit:
            conn.commit()
        return cursor

@app.route('/')
def index():
    query = 'SELECT id, x, y, z, r FROM axis ORDER BY id DESC LIMIT 1'
    ultima_linha = execute_query(query).fetchone()
    x, y, z, r = ultima_linha[1:]
    return render_template('index.html', x=x, y=y, z=z, r=r)

@app.route('/data', methods=['POST'])
def post():
    query = 'INSERT INTO axis (x, y, z, r) VALUES (?, ?, ?, ?)'
    args = (request.form['x'], request.form['y'], request.form['z'], request.form['r'])
    execute_query(query, args, commit=True)
    return redirect('/')

@app.route('/data', methods=['GET'])
def get():
    query = 'SELECT id, x, y, z, r FROM axis ORDER BY id DESC LIMIT 1'
    ultima_linha = execute_query(query).fetchone()
    my_dict = {'id': ultima_linha[0], 'x': ultima_linha[1], 'y': ultima_linha[2], 'z': ultima_linha[3], 'r': ultima_linha[4]}
    return jsonify(my_dict)


if __name__ == '__main__':
    app.run(debug=True)
