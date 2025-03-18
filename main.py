from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return 'Bem Vindo ao Bootcamp API'

@app.route("/alunos")
def get_alunos():
    alunos = ['Marcos', 'Maicon', 'Murilo']
    return alunos