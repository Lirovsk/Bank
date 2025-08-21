import os
from .database_works.info_and_stoarage.infoCretion import ClienteConfig
from database_works.info_and_stoarage.infoCretion import create_db, existing_engine

menu = """
selecione uma das opções:
1. Criar banco de dados
2. Usar banco de dados existente
3. Sair
"""
menu2 ="""
1. Criar conta pessoal
2. criar conta bancária
3. entrar no banco
4. sair
"""

menu3 = """
1. Depositar
2. Sacar
3. Transferir
4. voltar
"""

print(menu)
choice = input("Digite sua escolha: ")

if choice == "1":
    engine =create_db()

elif choice == "2":
    engine = existing_engine()


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(menu2)
    choice2 = input("Digite sua escolha: ")

    if choice2 == "1":
        ClienteConfig.create_client(engine)

    elif choice2 == "2":
        print("Criar conta bancária")

    elif choice2 == "3":
        # pedir para o usuário entrar na sua conta
        # pedir para o usuário entrar na sua conta bancária
        print("Entrar no banco")

    elif choice2 == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")


def banco(conta_id):
    while True:
        # print saldo
        print(menu3)
        choice = input("Digite sua escolha: ")

        if choice == "1":
            print("Depositar")

        elif choice == "2":
            print("Sacar")

        elif choice == "3":
            print("Transferir")

        elif choice == "4":
            print("Voltar")
            break
        else:
            print("Opção inválida.")
