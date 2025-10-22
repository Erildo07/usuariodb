import sqlite3

def conectar():
    return sqlite3.connect('clientes.db')

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    # tabela clientes
    c.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT,
            cpf TEXT,
            saldo REAL DEFAULT 0
        )
    ''')
    # tabela usuários
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    # cria usuário padrão
    c.execute("INSERT OR IGNORE INTO usuarios (id, username, password) VALUES (1,'admin','admin')")
    conn.commit()
    conn.close()

def verificar_usuario(username, password):
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios WHERE username=? AND password=?', (username, password))
    user = c.fetchone()
    conn.close()
    return user

def cadastrar_cliente(nome, email, cpf, saldo):
    conn = conectar()
    c = conn.cursor()
    c.execute('INSERT INTO clientes (nome, email, cpf, saldo) VALUES (?, ?, ?, ?)', (nome, email, cpf, saldo))
    conn.commit()
    conn.close()

def listar_clientes():
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM clientes')
    dados = c.fetchall()
    conn.close()
    return dados

def buscar_cliente(busca):
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM clientes WHERE nome LIKE ? OR email LIKE ? OR cpf LIKE ?', (f'%{busca}%', f'%{busca}%', f'%{busca}%'))
    dados = c.fetchall()
    conn.close()
    return dados

def editar_saldo(id_cliente, novo_saldo):
    conn = conectar()
    c = conn.cursor()
    c.execute('UPDATE clientes SET saldo=? WHERE id=?', (novo_saldo, id_cliente))
    conn.commit()
    conn.close()

def deletar_cliente(id_cliente):
    conn = conectar()
    c = conn.cursor()
    c.execute('DELETE FROM clientes WHERE id=?', (id_cliente,))
    conn.commit()
    conn.close()
