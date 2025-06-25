import os
os.system('cls')

usuarios = {}

def cadastrar():
    print("=== Cadastro de Novo Usuário ===")
    usuario = input("Escolha um nome de usuário: ")

    if usuario in usuarios:
        print("Usuário já existe! Tente outro nome.")
        return False

    senha = input("Escolha uma senha: ")
    usuarios[usuario] = senha
    print("Usuário cadastrado com sucesso!")
    return True

def login():
    print("=== Login ===")
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso!")
        return True
    else:
        print("Usuário ou senha incorretos.")
        return False

def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ").lower()

        if opcao == "cadastrar":
            cadastrar()
        elif opcao == "login":
            login()
        elif opcao == "sair":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()
