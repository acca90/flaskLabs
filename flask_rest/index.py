from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "PUDIM"

@app.route("/contato", methods=['GET'])
def get_contato_list():
    return "Lista de contatos"

@app.route("/contato/<int:pk>/", methods=['GET'])
def get_contato(pk):
    return "Busca de contato"

@app.route("/contato", methods=['POST'])
def post_contato():
    return "Cadastra contato"

@app.route("/contato/<int:pk>/", methods=['PUT'])
def put_contato(pk):
    return "Atualiza contato"

@app.route("/contato/<int:pk>/", methods=['DELETE'])
def delete_contato(pk):
    return "Deleta contato"


