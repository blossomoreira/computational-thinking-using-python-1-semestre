# Faça um programa que leia uma matriz 3x3 de inteiros e
#multiplique os elementos da diagonal principal da matriz por 
#um número k.Imprima a matriz na tela antes e depois da multiplicação.

matriz = []

for lin in range (0,3):
    linha = []
    for col in range(0,3):
        linha.append(int(input('Digite os elementos (9) da matriz 3x3: ')))
    matriz.append(linha)

for lin in range (0,3):
    print(matriz[lin])

k = int(input('Digite o valor de K: '))

for lin in range (0,3):
    for col in range (0,3):
        if lin == col:
            matriz[lin][col] = matriz[lin][col]*k

for lin in range (0,3):
    print(matriz[lin])