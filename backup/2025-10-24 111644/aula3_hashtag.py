# ----------------- INPUTS -----------------------

# nome = input('Escreva seu nome: ')

# faturamento = float(input('Qual foi o faturamento da empresa? '))
# custo = float(input('Qual foi o custo da empresa? '))

# imposto = faturamento * 0.1
# lucro = faturamento - custo
# margem_lucro = lucro / faturamento

# print("Nome:", nome.title())
# print(f"Faturamento: R$ {faturamento:.2f}")
# print(f"Custo: R$ {custo:.2f}")
# print(f"Lucro: R$ {lucro:.2f}")
# print(f"Margem de lucro: {margem_lucro:.0%}")

# ----------------- LISTAS -----------------------
vendas = [100, 450, 1500, 15, 25, 250, 700]

# SOMAR VENDAS
total_vendas = sum(vendas)
print(total_vendas)

# TAMANHO DA LISTA
tamanho_lista = len(vendas)
print(tamanho_lista)

# MAIOR E MENOR
maior_valor = max(vendas)
menor_valor = min(vendas)
print(maior_valor, menor_valor)

# PEGAR POSIÇÃO
print(vendas[0])

lista_produtos = ["iphone", "macbook", "ipad", "apple watch"]

# procurar_produto = input("Qual produto deseja procurar? ")
# print(procurar_produto.lower() in lista_produtos)

# ADICIONAR UM ITEM
lista_produtos.append("airpod")
print(lista_produtos)

# REMOVER UM ITEM
lista_produtos.remove("apple watch")
print(lista_produtos)

# EDITAR UM ITEM
lista_produtos[0] = "iphone16"
print(lista_produtos)

# CONTAGEM DA LISTA
lista_produtos = ["iphone", "macbook", "ipad", "apple watch", "iphone", "ipad", "iphone"]
print(lista_produtos.count("airpod"))


# ORDENAR UMA LISTA
lista_produtos.sort()
print(lista_produtos)