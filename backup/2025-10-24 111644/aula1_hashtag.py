faturamento = 8202 #VARIÁVEL TIPO INT
custo = 364.86 #VARIÁVEL TIPO FLOAT
novas_vendas = 150
novas_vendas = faturamento + novas_vendas
imposto = faturamento * 0.1
lucro = faturamento - custo
margem_lucro = lucro / faturamento

print("O faturamento foi de:", faturamento)
print("O custo foi de:", custo)
print("O lucro foi de:", lucro)
print("A margem de lucro foi de:", round(margem_lucro, 2))

mensagem = "Obrigado!" #VARIÁVEL TIPO STRING
teve_lucro = True #VARIÁVEL TIPO BOOLEAN