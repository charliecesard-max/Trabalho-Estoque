try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError:
    pd = None
    plt = None

def estoque_de_itens(estoque):
    id = int(input('Digite o Código do produto:'))
    nome = str(input('Digite o nome do produto: '))
    categoria = str(input('Digite a categoria do produto:'))
    preco = float(input('Digite o preço do produto: '))
    unidade = int(input('Digite a unidade/quantidade do produto: '))
    estoque[id] = {'id': id, 'nome': nome, 'categoria': categoria, 'preco': preco, 'unidade': unidade}
    print(f'Produto {nome} cadastrado com sucesso!')

    print('Estoque Atual')
    for id, dados in reversed(list(estoque.items())):
        nome = dados['nome']
        categoria = dados['categoria']
        unidade = dados['unidade']
        print(f'{id}, {nome}, {categoria}, {unidade}')


def excluir(estoque):
    nome = input("Digite o nome do produto a ser excluído: ")
    if nome in estoque:
        del estoque[nome]
        print(f"Produto {nome} excluído com sucesso!")
    else:
        print("Produto não encontrado.")


def visualizar(estoque):
    df = pd.DataFrame(estoque.values())

    # calcular valor total
    df["valor_total"] = df["preco"] * df["unidade"]

    # agrupar por categoria
    df_cat = df.groupby("categoria")["valor_total"].sum().reset_index()

    # ordenar do maior para o menor
    df_cat = df_cat.sort_values("valor_total", ascending=True)

    # calcular percentuais
    valor_total_geral = df_cat["valor_total"].sum()
    df_cat["percentual"] = (df_cat["valor_total"] / valor_total_geral) * 100

    # acumulado
    df_cat["acumulado"] = df_cat["percentual"].cumsum()

    # gráfico
    plt.figure(figsize=(12,6))

    # cores ABC por categoria
    cores = []
    for v in df_cat["acumulado"]:
        if v <= 80:
            cores.append("#ff6666")  # A
        elif v <= 95:
            cores.append("#66b3ff")  # B
        else:
            cores.append("#ffb266")  # C

    # barras
    plt.bar(df_cat["categoria"], df_cat["percentual"], color=cores)

    # linha acumulada
    plt.plot(df_cat["categoria"], df_cat["acumulado"], marker="o", color="black", linewidth=2)

    # linhas horizontais pretas
    plt.axhline(80, color="black", linestyle="--", linewidth=1)
    plt.axhline(95, color="black", linestyle="--", linewidth=1)

    # títulos e textos
    plt.title("Curva ABC por Categoria (Proporção no Valor Total do Estoque)")
    plt.ylabel("Percentual (%)")
    plt.xticks(rotation=45)

    # rótulos nos pontos
    for i, v in enumerate(df_cat["acumulado"]):
        plt.text(i, v + 1, f"{v:.1f}%", ha="center")

    plt.tight_layout()
    plt.show()

def menu_estoque():       
    estoque = {}

    print("Qual opção deseja?")

    print("1 - Cadastrar Produto")
    print("2 - Excluir Produto")
    print("3 - Visualizar Lista de produtos")
    print("4 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    while opcao != 4:

        if opcao == 1:
            print("Cadastrar Produto")
            estoque_de_itens(estoque)

        elif opcao == 2:
            print("Excluir Produto")
            excluir(estoque)

        elif opcao == 3:
            print("\nRelatório de Produtos Cadastrados:")
            visualizar(estoque)

        opcao = int(input("Digite a opção desejada: "))

    print("Saindo...")

