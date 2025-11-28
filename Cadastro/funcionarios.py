import pandas as pd

def criar_lista(listas):
    nome_lista = input("Digite o nome da nova lista de funcionários: ")
    if nome_lista in listas:
        print("Essa lista já existe.\n")
    else:
        listas[nome_lista] = {}
        print(f"Lista '{nome_lista}' criada com sucesso!\n")


def abrir_lista(listas):
    if not listas:
        print("Nenhuma lista existente. Crie uma primeiro.\n")
        return None
    print("\nListas disponíveis:")
    for nome in listas.keys():
        print(f"- {nome}")
    nome_lista = input("Digite o nome da lista que deseja abrir: ")
    if nome_lista in listas:
        print(f"Lista '{nome_lista}' aberta com sucesso!\n")
        return nome_lista
    else:
        print("Lista não encontrada.\n")
        return None


def adicionar_funcionario(listas, lista_atual):
    if not lista_atual:
        print("Nenhuma lista aberta. Abra uma lista primeiro.\n")
        return
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário (use ponto para decimais): "))
    listas[lista_atual][nome] = {"salario": salario}
    print(f"Funcionário {nome} cadastrado com sucesso na lista '{lista_atual}'!\n")


def listar_funcionarios(listas, lista_atual):
    if not lista_atual:
        print("Nenhuma lista aberta.\n")
        return
    
    funcionarios = listas[lista_atual]
    
    if not funcionarios:
        print("Nenhum funcionário cadastrado nessa lista.\n")
    else:
        print(f"\n--- Lista de Funcionários ({lista_atual}) ---")

        # Converte dicionário em DataFrame
        df = pd.DataFrame.from_dict(funcionarios, orient='index')
        df.index.name = "Nome"

        # Mostra no terminal
        print(df.to_string())
        print()

        # Nome do arquivo
        nome_arquivo = f"lista_{lista_atual}.xlsx"

        # Salva em Excel
        df.to_excel(nome_arquivo, index=True)

        print(f"Arquivo Excel '{nome_arquivo}' gerado com sucesso!\n")


def buscar_funcionario(listas, lista_atual):
    if not lista_atual:
        print("Nenhuma lista aberta.\n")
        return
    funcionarios = listas[lista_atual]
    if not funcionarios:
        print("Nenhum funcionário cadastrado nessa lista.\n")
        return
    nome = input("Digite o nome do funcionário que deseja buscar: ")
    if nome in funcionarios:
        print(f"Funcionário encontrado: {nome} — Salário: R$ {funcionarios[nome]['salario']:.2f}\n")
    else:
        print("Funcionário não encontrado.\n")


def editar_funcionario(listas, lista_atual):
    if not lista_atual:
        print("Nenhuma lista aberta.\n")
        return
    funcionarios = listas[lista_atual]
    if not funcionarios:
        print("Nenhum funcionário cadastrado nessa lista.\n")
        return
    nome = input("Digite o nome do funcionário que deseja editar: ")
    if nome in funcionarios:
        print(f"Funcionário atual: {nome} — Salário: R$ {funcionarios[nome]['salario']:.2f}")
        novo_nome = input("Digite o novo nome (ou pressione Enter para manter): ")
        novo_salario_input = input("Digite o novo salário (ou pressione Enter para manter): ")

        if novo_nome:
            funcionarios[novo_nome] = funcionarios.pop(nome)
            nome = novo_nome

        if novo_salario_input:
            funcionarios[nome]["salario"] = float(novo_salario_input)

        print(f"Funcionário '{nome}' atualizado com sucesso!\n")
    else:
        print("Funcionário não encontrado.\n")


def calcular_media_salarial(listas, lista_atual):
    if not lista_atual:
        print("Nenhuma lista aberta.\n")
        return
    funcionarios = listas[lista_atual]
    if not funcionarios:
        print("Nenhum funcionário cadastrado nessa lista.\n")
        return
    total = sum(dados["salario"] for dados in funcionarios.values())
    media = total / len(funcionarios)
    print(f"Média salarial dos funcionários da lista '{lista_atual}': R$ {media:.2f}\n")


def menu_funcionarios():
    listas = {}
    lista_atual = None

    print("=== SISTEMA DE GERENCIAMENTO DE FUNCIONÁRIOS ===")

    while True:
        print("\nQual opção deseja?")
        print("1 - Criar Nova Lista de Funcionários")
        print("2 - Abrir Lista Existente")
        print("3 - Cadastrar Funcionário")
        print("4 - Listar Funcionários")
        print("5 - Buscar Funcionário por Nome")
        print("6 - Editar Funcionário")
        print("7 - Calcular Média Salarial")
        print("8 - Sair")

        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Por favor, digite um número válido.\n")
            continue

        if opcao == 1:
            criar_lista(listas)
        elif opcao == 2:
            lista_atual = abrir_lista(listas)
        elif opcao == 3:
            adicionar_funcionario(listas, lista_atual)
        elif opcao == 4:
            listar_funcionarios(listas, lista_atual)
        elif opcao == 5:
            buscar_funcionario(listas, lista_atual)
        elif opcao == 6:
            editar_funcionario(listas, lista_atual)
        elif opcao == 7:
            calcular_media_salarial(listas, lista_atual)
        elif opcao == 8:
            print("Saindo do sistema... Até mais!")
            break
        else:
            print("Opção inválida, tente novamente.\n")
