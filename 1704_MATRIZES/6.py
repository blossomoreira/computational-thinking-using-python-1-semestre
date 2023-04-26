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

#elementos da lista a + 5

for elementosListaA in range(0,10):
    elementosA = int(input('10 elementos: '))
    elementosACol0 = elementosA + 5
    elementosACol1 = elementosA * 3
    elementosACol2 = elementosA ** 2
    listaA.append([elementosACol0, elementosACol1, elementosACol2])


print(listaA[0])


#criando matriz
for lin in range (0,10):
    linha = []
    for col in range (0,3):
        linha.append(listaA)
    matrizC.append(listaA)


print(matrizC[lin])