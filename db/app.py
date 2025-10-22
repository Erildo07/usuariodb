from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import database

app = Flask(__name__)
database.criar_tabela()

@app.route('/styles/<path:filename>')
def custom_styles(filename):
    return send_from_directory(os.path.join(app.root_path, 'styles'), filename)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if database.verificar_usuario(username, password):
        return redirect(url_for('menu'))
    else:
        return "❌ Usuário ou senha incorretos!"

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        saldo = request.form['saldo']
        database.cadastrar_cliente(nome, email, cpf, saldo)
        return redirect(url_for('menu'))
    return render_template('cadastrar.html')

@app.route('/listar')
def listar():
    clientes = database.listar_clientes()
    return render_template('listar.html', clientes=clientes)

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    resultados = []
    if request.method == 'POST':
        busca = request.form['busca']
        resultados = database.buscar_cliente(busca)
    return render_template('buscar.html', resultados=resultados)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        novo_saldo = float(request.form['saldo'])
        database.editar_saldo(id, novo_saldo)
        return redirect(url_for('listar'))
    return render_template('editar.html', id=id)


@app.route('/deletar', methods=['GET', 'POST'])
def deletar():
    if request.method == 'POST':
        id_cliente = request.form['id']
        database.deletar_cliente(id_cliente)
        return redirect(url_for('menu'))
    return render_template('deletar.html')

if __name__ == '__main__':
    app.run(debug=True)
