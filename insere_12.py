# insere_12.py - insere 12 clientes com saldo fictício
from db import database

database.criar_tabela()

clientes = [
    ("Lucas Silva", "335.326.626-71", "lucas.silva807@gmail.com", 120.50),
    ("Mariana Souza", "812.125.020-00", "mariana.souza916@gmail.com", 250.00),
    ("Gustavo Oliveira", "046.944.579-34", "gustavo.oliveira192@gmail.com", 75.20),
    ("Beatriz Pereira", "028.146.157-00", "beatriz.pereira586@gmail.com", 980.00),
    ("Felipe Lima", "421.142.784-92", "felipe.lima51@gmail.com", 10.00),
    ("Renata Gomes", "927.541.063-16", "renata.gomes274@gmail.com", 430.75),
    ("Carlos Ribeiro", "992.594.352-34", "carlos.ribeiro45@gmail.com", 5.00),
    ("Viviane Almeida", "858.658.818-09", "viviane.almeida295@gmail.com", 600.00),
    ("Joao Ferreira", "702.424.318-01", "joao.ferreira271@gmail.com", 300.40),
    ("Larissa Costa", "833.152.185-44", "larissa.costa2@gmail.com", 0.00),
    ("Andre Rocha", "775.385.066-08", "andre.rocha537@gmail.com", 45.90),
    ("Paula Carvalho", "968.069.295-75", "paula.carvalho418@gmail.com", 210.00),
]

inserted = 0
for nome, cpf, email, saldo in clientes:
    try:
        database.cadastrar_cliente(nome, email, cpf, saldo)
        print(f"ok: {nome}")
        inserted += 1
    except Exception as e:
        print(f"erro ao inserir {nome}: {e}")

print(f"\nInserção concluída. Total inserido: {inserted} registros.")
