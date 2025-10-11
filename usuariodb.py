print("REGISTRO DE CLIENTES")
print("----***----")
print("Digite um número: ")
print("1 - Digite para criar :")
print("2 - Degitar para editar :")
print("3 - Digite para deletar :")
print("4 - Digite para sair...")

while True:

    opcao = input("escoha uma opção.")

    if opcao == "1":
        print("Você escolheu 1 opção para cria Usuario:")
    elif opcao == "2":
        print("Essa 2 opção é para editar nome:")
    elif opcao == "3":
        print("Deletar 3 opcão Usuário: ")
    elif opcao == "4":
        print("Saindo...")
        break
    else: 
        print("Tente novamente ! ! !")