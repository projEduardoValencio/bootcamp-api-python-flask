from main import app

@app.route("/")
def inicio():
    return 'Bem Vindo ao Bootcamp API'

@app.route("/alunos", methods=["GET"])
def get_alunos():
    # alunos = ['Marcos', 'Maicon', 'Murilo']
    return 'NULL'