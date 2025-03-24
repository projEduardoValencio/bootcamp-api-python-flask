from main import app
from dbmanager import DBManager

database = DBManager("db/BD_Bootcamp.db")

@app.route("/")
def inicio():
    return 'Bem Vindo ao Bootcamp API'

@app.route("/alunos")
def get_alunos():
    
    return 'NULL'