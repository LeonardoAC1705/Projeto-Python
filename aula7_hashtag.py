lista_precos = [1500, 1000, 800, 3000]

# Imposto
# Aliquota1 -> IR = 0.2
# Aliquota2 -> IR = 0.15
# Aliquota3 -> CSLL = 0.05

def calcula_imposto_total(preco):
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco
        
    imposto_iss = 0.15 * preco
    imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll    
    return imposto_total


for preco in lista_precos:
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco
    imposto_iss = 0.15 * preco
    imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    print(f"Imposto total sobre o produto de R$ {preco}: R${imposto_total}")
    print()
    preco_final = preco - imposto_total
    print(f"Valor Final sobre o produto de R$ {preco}: R${preco_final}")