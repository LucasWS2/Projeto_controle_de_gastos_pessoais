from database import create_table
from gastos import adicionar_gasto, listar_gastos, total_gastos

create_table()

def menu():
    while True:
        print("\n1. Adicionar gasto")
        print("2. Listar gastos")
        print("3. Ver total de gastos")
        print("4. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            descricao = input("Descrição: ")
            valor = float(input("Valor: R$ "))
            categoria = input("Categoria: ")
            adicionar_gasto(descricao, valor, categoria)
            print("✅ Gasto registrado!")
        elif opcao == "2":
            for g in listar_gastos():
                print(f"{g[0]} | {g[1]} | R$ {g[2]:.2f} | {g[3]} | {g[4]}")
        elif opcao == "3":
            print(f"💰 Total: R$ {total_gastos():.2f}")
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

menu()
