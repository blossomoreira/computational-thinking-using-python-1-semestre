#Faça um programa em Python que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos
#cujos valores deverão ser compostos pelos elementos intercalados das 2 listas.

listaA = []
listaB = []
listaC = []

for i in range (10):
    listaA.append(int(input("Digite um numero na lista A")))
    listaB.append(int(input("Digite um numero na lista B")))

for i in range (20):
    listaC.append(listaA[i])
    listaC.append(listaB[i])

print(listaA)
print(listaB)
print(listaC)