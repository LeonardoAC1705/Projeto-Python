# --------------------------------- IF E LOGICA DE CONDIÇÕES ----------------------------------------

vendas = int(input("Qual o valor da venda? "))
meta1 = 1300 #---> 10%
meta2 = 2000 #---> 15%

# > MAIOR QUE
# < MENOR QUE
# >= MAIOR OU IGUAL
# <= MENOR O IGUAL
# == IGUAL
# != DIFERENTE

# if vendas > meta1:
#     print("Parabéns! Você ganhou bonus!!")
#     bonus = vendas * 0.1
#     print("Bonus da venda: R$", bonus)
# else:
#     print("Que pena! Você não ganhou bonus")


# 2º CENÁRIO
if vendas >= 2000:
    bonus = 0.15 * vendas
elif vendas >= 1300:
    bonus = 0.1 * vendas
else:
    bonus = 0
    
print("Bonus:", bonus)

# 3° CENÁRIO
lista_produtos = ["iphone", "macbook", "airpod", "ipad"]
procurar_produto = input("Procure um produto: ")
procurar_produto = procurar_produto.lower()

if procurar_produto in lista_produtos:
    print("Produto no estoque")
else:
    print("Não temos este produto")
    
    

    
