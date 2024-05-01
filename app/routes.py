from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/cadastro")
def cadastrofuncionario():
    return render_template("cadastroc.html")
