listaA = []
listaB = []
listaC = []

for i in range (3):
    listaA.append(int(input("Digite um numero da lista A: ")))
    listaB.append(int(input("Digite um numero da lista B: ")))

for i in range (3):
    listaC.append(listaA[i])
    listaC.append(listaB[i])

print(listaA)
print(listaB)
print(listaC)

