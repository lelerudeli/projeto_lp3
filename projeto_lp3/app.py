from flask import Flask, render_template
from projeto_lp3.validations import *


app = Flask(__name__)

# rota + função

# / - home page
@app.route("/")

def home():
    return render_template ("home.html")


# /contato - pagina de contato 
@app.route("/contato")

def contato():
    return render_template ("contato.html")


# /produtos - pagina produtos 
@app.route("/produtos")

def produtos():
    lista_produtos = [
        {"nome": "coquinha bb", "desc": "ruim"},
        {"nome": "doritos", "desc": "suja a mao"},
        {"nome": "sneakers", "desc": "meu choc preferido"}
    ]

    return render_template ("produtos.html", produtos = lista_produtos)

@app.route("/cpfcnpj")
def cpf():
    cpf = validaCpf()
    cnpj = validaCnpj()
    return render_template("cpfcnpj.html", cpf=cpf, cnpj=cnpj)

@app.route("/cadastro")
def cadastro_produtos():
    return render_template("cadastro_produtos.html")

@app.route("/comousar")
def como_usar():
    return render_template("como_usar.html")

@app.route("/politicas")
def politicas():
    return render_template("politica.html")

@app.route("/termos")
def termos():
     return render_template("termos.html")

app.run(debug=True)