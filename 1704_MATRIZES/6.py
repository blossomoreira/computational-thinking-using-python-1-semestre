'''
Escreva um programa que leia uma lista A com 10 elementos.

Construir uma matriz C com três colunas, 

a primeira coluna da matriz C é formada pelos elementos da lista A
somados com mais 5,


a segunda coluna é formada pelo triplo de cada elemento
correspondente da lista A


e a terceira e última coluna deve ser formada pelos quadrados dos elementos
correspondentes da lista A. Por fim, mostre os elementos da matriz C.
'''


listaA = []
matrizC = []

for i in range(10):
    listaA.append(int(input("Digite um elemento da lista: ")))

for i in range(10):
    linha = []
    linha.append(listaA[i] + 5)
    linha.append(listaA[i] * 3)
    linha.append(listaA[i]**2)
    matrizC.append(linha)

print(listaA)

for i in range(10):
    print(matrizC[i])