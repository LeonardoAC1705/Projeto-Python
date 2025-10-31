# --------------------------- STRINGS E FUNÇÕES DE TEXTO ------------------------------------------

faturamento = 1200
custo = 300
lucro = faturamento - custo
margem_lucro = lucro / faturamento

print(f"O faturamento foi de: {faturamento}, o custo foi de: {custo}, o lucro foi de: {lucro}")

email_cliente = 'leoandradecerqueira@GMAIL.COM'

# TRANSFORMAR EM LETRA MAIÚSCULA
email_cliente = email_cliente.upper()
print("Letra maiúscula:", email_cliente)

# TRANSFORMAR EM LETRA MINÚSCULA
email_cliente = email_cliente.lower()
print("Letra minúscula:", email_cliente)

# LOCALIZAR CARACTER
print("Localizar caracter:", email_cliente.find('@')) # -1 QUANDO NÃO ENCONTRAR

# TAMANHO DO TEXTO
print("Tamanho do texto:", len(email_cliente))

print('')

# PEGAR UM CARACTER
print("Pegando um caracter:", email_cliente[19])
print("Pegando um caracter (negativo):", email_cliente[-10]) # DE TRÁS PRA FRENTE

# PEGAR UM RECORTE DO TEXTO
print("Pegando um recorte do texto:", email_cliente[:3]) # DO COMEÇO
print("Pegando um recorte do texto:", email_cliente[3:19]) # NO MEIO 
print("Pegando um recorte do texto:", email_cliente[19:]) # ATÉ O FINAL

print('')

# ALTERAR O TEXTO
novo_email = email_cliente.replace('gmail', 'hotmail')
print(novo_email) 

# TRABALHANDO COM NOMES
nome = 'leonardo andrade cerqueira'
print("Primeira letra maiúscula:", nome.capitalize()) # APENAS A PRIMEIRA LETRA MAIÚSCULA
print("Início de palavras com letras maiúsculas:", nome.title()) # TODAS LETRAS INICIAIS MAIÚSCULAS

# PEGAR SERVIDOR
arroba = email_cliente.find('@') + 1
servidor = email_cliente[arroba:]
print("Pegando servidor:", servidor)

# PRIMEIRO NOME
espaco = nome.find(' ')
primeiro_nome = nome[:espaco]
print("Primeiro Nome:", primeiro_nome.capitalize())

# SEGUNDO NOME
espaco = nome.find(' ')
sobrenome = nome[espaco + 1:]
print("Sobrenome:", sobrenome.title())

print('')

# FORMATAÇÃO NUMÉRICA EM TEXTO
margem_lucro = round(margem_lucro, 2)
print(f"O faturamento foi de: R${faturamento:.2f}\nO custo foi de: R${custo:.2f}\nO lucro foi de: R${lucro:.2f}\nA margem de lucro foi de: {margem_lucro:.0%}")





