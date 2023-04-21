#· Faça um programa que leia uma matriz 3x3 de inteiros
# e multiplique os elementos da diagonal principal da matriz por um número k.
# Imprima a matriz na tela antes e depois da multiplicação.

matriz = []
for lin in range(0,3):
    linha = []
    for col in range(0,3):
        linha.append(int(input('Digite os elementos aqui')))
    matriz.append(linha)
print(matriz)

k = int(input('Digite o valor de K'))
for lin in range(0,3):
    for col in range(0,3):
        if lin == col:                  #se a posição linha for igual a coluna
            matriz[col][lin] = matriz[col][lin] * k #os elementos vão se multiplicados pelo úmerp inputado

for lin in range(0,3): #imprimindo matriz inteira
    print(matriz[lin])

