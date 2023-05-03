'''
Escreva um programa em Python para ler 15 elementos de uma lista A.

Construir uma lista B, observando a seguinte lei de formação:
Todo elemento de B deve ser o quadrado do elemento de A correspondente.
Apresentar as listas A e B.
'''

listaA = []
listaB = []

for i in range (0,3):
    elementosinputados = int(input(''))
    listaA.append(elementosinputados)
    listaB.append(elementosinputados**elementosinputados)
print(listaB)