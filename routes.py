from main import app

@app.route("/")
def inicio():
    return 'Bem Vindo ao Bootcamp API'

@app.route("/alunos")
def get_alunos():
    alunos = ['Marcos', 'Maicon', 'Murilo']
    return alunos