from flask import Flask, request, jsonify, render_template, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base
from models.axis import Axis

app = Flask(__name__)

# Define a conexão com o banco de dados
DATABASE_URL = 'sqlite:///database.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Rota principal, que exibe a última linha da tabela 'axis'
@app.route('/')
def index():
    try:        
        session = Session()
        last_entry = session.query(Axis).order_by(Axis.id.desc()).first()
        x, y, z = last_entry.x, last_entry.y, last_entry.z
        session.close()
        
    except:
        x, y, z = 0, 0, 0

    return render_template('index.html', x=x, y=y, z=z)

# Rota para receber os dados do formulário via POST e inseri-los na tabela 'axis'
@app.route('/data', methods=['POST'])
def post():
    x, y, z = int(request.form['x']), int(request.form['y']), int(request.form['z'])
    new_entry = Axis(x=x, y=y, z=z)
    session = Session()
    session.add(new_entry)
    session.commit()
    return redirect('/')

# Rota para retornar a última linha da tabela 'axis' como um objeto JSON
@app.route('/data', methods=['GET'])
def get():
    session = Session()
    last_entry = session.query(Axis).order_by(Axis.id.desc()).first()
    response = {'id': last_entry.id, 'x': last_entry.x, 'y': last_entry.y, 'z': last_entry.z, 'r': last_entry.r}
    return jsonify(response)

# Executa o servidor Flask
if __name__ == '__main__':
    Base.metadata.create_all(bind = engine) 
    app.run(debug=True)
