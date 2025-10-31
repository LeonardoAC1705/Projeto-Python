import matplotlib.pyplot as plt

inicio = int(input("Insira o início do intervalo: "))
fim = int(input("Insira o fim do intervalo: "))

numeros = list(range(inicio, fim + 1))
quadrados = [x**2 for x in numeros]

plt.plot(numeros, quadrados, marker='o')
plt.title("Números e seus Quadrados")
plt.xlabel("Números")
plt.ylabel("Quadrados")
plt.grid(True)
plt.show()
