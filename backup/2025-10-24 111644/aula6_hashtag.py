dic_produtos = {"iphone": 6000, "airpod": 1000, "ipad": 8000, "macbook": 11000}

# Pegar um elemento
print(dic_produtos["iphone"])

# Editar um elemento
dic_produtos["iphone"] = dic_produtos["iphone"] + 500
print(dic_produtos)

# Quantidade de itens
print(len(dic_produtos))

# Adicionar um item
dic_produtos["apple watch"] = 2500
print(dic_produtos)


nome_produto = input("Nome do produto: ")
preco_produto = input("Preço do produto: ")

dic_produtos[nome_produto] = preco_produto
print(dic_produtos) 
