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
        saldo = input("Saldo inicial (R$): ")
        try:
            saldo = float(saldo)
        except ValueError:
            saldo = 0.0
        database.cadastrar_cliente(nome, email, cpf, saldo)
        print("✅ Cliente cadastrado com sucesso!")

    elif opcao == "2":
        clientes = database.listar_clientes()
        if clientes:
            print("\n=== CLIENTES CADASTRADOS ===")
            for c in clientes:
                idc = c[0]
                nome = c[1] or ""
                email = c[2] or ""
                cpf = c[3] or ""
                saldo = float(c[4]) if c[4] is not None else 0.0
                print(f"ID: {idc} | Nome: {nome} | Email: {email} | CPF: {cpf} | Saldo: R${saldo:.2f}")
        else:
            print("Nenhum cliente encontrado.")

    elif opcao == "3":
        termo = input("Digite nome, e-mail ou CPF para buscar: ")
        resultados = database.buscar_cliente(termo)
        if resultados:
            print("\n=== RESULTADOS DA BUSCA ===")
            for r in resultados:
                idc = r[0]
                nome = r[1] or ""
                email = r[2] or ""
                cpf = r[3] or ""
                saldo = float(r[4]) if r[4] is not None else 0.0
                print(f"ID: {idc} | Nome: {nome} | Email: {email} | CPF: {cpf} | Saldo: R${saldo:.2f}")
        else:
            print("⚠️ Nenhum cliente encontrado com esse termo.")

    elif opcao == "4":
        id_cliente = input("Digite o ID do cliente: ")
        novo_saldo = input("Novo saldo (R$): ")
        try:
            novo_saldo = float(novo_saldo)
            database.editar_saldo(id_cliente, novo_saldo)
            print("✅ Saldo atualizado com sucesso!")
        except ValueError:
            print("⚠️ Valor inválido para saldo.")

    elif opcao == "5":
        id_cliente = input("Digite o ID do cliente a ser deletado: ")
        database.deletar_cliente(id_cliente)
        print("🗑️ Cliente deletado com sucesso!")

    elif opcao == "6":
        print("👋 Saindo do sistema...")
        break

    else:
        print("❌ Opção inválida! Tente novamente.")
