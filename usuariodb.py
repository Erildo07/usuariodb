from db import database

database.criar_tabela()

print("=== SISTEMA DE CLIENTES ===")

while True:
    print("\n1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente (por nome, e-mail ou CPF)")
    print("4 - Editar saldo do cliente")
    print("5 - Deletar cliente")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        cpf = input("CPF: ")
        database.inserir_cliente(nome, email, cpf)
        print("✅ Cliente cadastrado com sucesso!")

    elif opcao == "2":
        clientes = database.listar_clientes()
        if clientes:
            print("\n=== CLIENTES CADASTRADOS ===")
            for c in clientes:
                print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]} | CPF: {c[3]} | Saldo: R${c[4]:.2f}")
        else:
            print("Nenhum cliente encontrado.")

    elif opcao == "3":
        termo = input("Digite nome, e-mail ou CPF para buscar: ")
        resultados = database.buscar_cliente(termo)
        if resultados:
            print("\n=== RESULTADOS DA BUSCA ===")
            for r in resultados:
                print(f"ID: {r[0]} | Nome: {r[1]} | Email: {r[2]} | CPF: {r[3]} | Saldo: R${r[4]:.2f}")
        else:
            print("⚠️ Nenhum cliente encontrado com esse termo.")

    elif opcao == "4":
        id_cliente = input("ID do cliente: ")
        novo_saldo = float(input("Novo saldo: R$"))
        database.atualizar_saldo(id_cliente, novo_saldo)
        print("💰 Saldo atualizado com sucesso!")

    elif opcao == "5":
        id_cliente = input("ID do cliente a ser deletado: ")
        database.deletar_cliente(id_cliente)
        print("🗑️ Cliente deletado com sucesso!")

    elif opcao == "6":
        print("Saindo...")
        break

    else:
        print("❌ Opção inválida! Tente novamente.")
