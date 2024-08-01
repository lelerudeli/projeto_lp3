from flask import Flask, render_template, request
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
        { "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQm4S15squn95k7qtrVOpMX1MOJGe48y4B7FQ&s", "nome": "Coca Cola", "desc": "Mata a sede e você"},
        { "img": "https://giassi.vtexassets.com/arquivos/ids/1163835-800-auto?v=638510248118900000&width=800&height=auto&aspect=true", "nome": "Doritos", "desc": "Suja a mao"},
        { "img": "https://media.istockphoto.com/id/529240903/pt/foto/barra-de-chocolate-snickers-isolado-em-fundo-branco.jpg?s=612x612&w=0&k=20&c=iXWRNpoTFmX_24oq-hsDG7ULfqqJ7lIEt9gH5eMzFuI=", "nome": "Snikers", "desc": "Meu chocolate preferido"}
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
    return render_template("politicas.html")

@app.route("/termos")
def termos():
     return render_template("termos.html")

# @app.route("/produtos", methods = ["POST"])
# def salvar_produto():
#     #pegando os valores digitados no form
#     #que estão na request
#     nome = request.form["nome"]
#     descricao = request.form["descricao"]
    
#     #crio um novo dictionary/produto
#     produto = {"nome": nome, "descricao": descricao, "url": ""}
    
#     #adiciona na lista esse novo produto
#     produtos.append(produto)
    
#     #retorna o template já com o novo produto cadastrado
#     return render_template("produto.html", produtos = produtos)

app.run(debug=True)