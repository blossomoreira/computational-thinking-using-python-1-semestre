'''
Escreva um programa para ler uma matriz A com 8 linhas e 6 colunas.
Construir uma lista B que seja formado pela soma de cada linha da matriz A.
Ao final apresentar o somatório dos elementos da lista B.
'''

matriz = []
listaB = []

for lin in range (0,3):
    linha = []
    for col in range (0,3):
        elementos = int(input('Digite os elementos'))
        linha.append(elementos)
    matriz.append(linha)

for lin in range (0,3):
    print(matriz[lin])

#somandolinhas
for lin in range (0,3):
    somalinhas = 0
    for col in range (0,3):
        somalinhas = matriz[lin][col] + somalinhas
    listaB.append(somalinhas)
print(listaB)