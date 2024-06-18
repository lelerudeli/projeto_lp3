from flask import Flask, render_template

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

    return render_template ("produtos.html", produtos=lista_produtos)