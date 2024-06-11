from flask import Flask 

app = Flask("Minha App")

# rota + função

# / - home page
@app.route("/")

def home():
    return "<h1>Home Page </h1>"

# /Perfil - conta usuario
@app.route("/Perfil")

def contato():
    return "<h1>Sua conta</h1>"



# /contato - pagina de contato 
@app.route("/contato")

def contato():
    return "<h1>xaaaama bb *foguinho *foguinho</h1>"


# /produtos - pagina produtos 
@app.route("/produtos")

def produtos():
    return "<h1> meus produtinhooos</h1>"
