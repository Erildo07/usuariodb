import os
import sqlite3

# Caminho do banco
pasta_db = os.path.dirname(__file__)
arquivo_db = os.path.join(pasta_db, "clientes.db")

# Conexão
def conectar():
    if not os.path.exists(pasta_db):
        os.makedirs(pasta_db)
    conexao = sqlite3.connect(arquivo_db)
    return conexao

# Criar tabela
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT,
            cpf TEXT UNIQUE,
            saldo REAL DEFAULT 0
        )
    """)
    conexao.commit()
    conexao.close()

# Inserir cliente
def inserir_cliente(nome, email, cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, email, cpf) VALUES (?, ?, ?)", (nome, email, cpf))
    conexao.commit()
    conexao.close()

# Listar todos os clientes
def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, email, cpf, saldo FROM clientes")
    dados = cursor.fetchall()
    conexao.close()
    return dados

# Buscar por nome ou email ou CPF
def buscar_cliente(termo):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id, nome, email, cpf, saldo FROM clientes
        WHERE nome LIKE ? OR email LIKE ? OR cpf LIKE ?
    """, (f"%{termo}%", f"%{termo}%", f"%{termo}%"))
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

# Atualizar saldo
def atualizar_saldo(id_cliente, novo_saldo):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE clientes SET saldo = ? WHERE id = ?", (novo_saldo, id_cliente))
    conexao.commit()
    conexao.close()

# Deletar cliente
def deletar_cliente(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    conexao.commit()
    conexao.close()
