import funcionarios
import estoque

def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Sistema de Funcionários")
        print("2 - Sistema de Estoque")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            funcionarios.menu_funcionarios()
        elif opcao == "2":
            estoque.menu_estoque()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    main()