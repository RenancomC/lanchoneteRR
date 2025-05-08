from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/bebida')
def bebida():
    return render_template('bebida.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

@app.route('/criarLanche')
def criarLanche():
    return render_template('criarLanche.html')

@app.route('/cupom')
def cupom():
    return render_template('cupom.html')

@app.route('/dadoPessoal')
def dadoPessoal():
    return render_template('dadoPessoal.html')

@app.route('/guarnicao')
def guarnicao():
    return render_template('guarnicao.html')

@app.route('/infoproduto')
def infoproduto():
    return render_template('infoproduto.html')

@app.route('/lanche')
def lanche():
    return render_template('lanche.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/pagamento')
def pagamento():
    return render_template('pagamento.html')

@app.route('/sobremesa')
def sobremesa():
    return render_template('sobremesa.html')

if __name__ == "__main__":
    app.run(debug=True)