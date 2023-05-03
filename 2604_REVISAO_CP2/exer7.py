'''
Escreva um programa em Python que leia uma matriz M [5x5] e,
a cada linha, multiplique cada elemento pelo valor do elemento
inserido na diagonal principal da linha. Os elementos da matriz
serão fornecidos pelo usuário. Escrever a matriz M lida e a matriz M
modificada.
'''
matriz = []

for lin in range (0,3):
    linha = []
    for col in range (0,3):
        linha.append(int(input('Digite o valor dos elementos')))
    matriz.append(linha)

for lin in range (0,3):
    print(matriz[lin])

for lin in range (0,3):
    for col in range (0,3):
        if lin == col:
            matriz[col][lin] = matriz[col][lin] * 2

for lin in range (0,3):
    print(matriz[lin])


