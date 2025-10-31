lista_vendas = [1000, 500, 800, 1500, 3000, 2300]

meta = 1500
bonus = 0.1

for venda in lista_vendas:
    if venda >= 1500:
        bonus = 0.1 * venda
    else:
        bonus = 0
    print(bonus)