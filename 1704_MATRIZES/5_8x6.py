'''
Escreva um programa para ler uma matriz A com 8 linhas e 6 colunas.
Construir uma lista B que seja 
formado pela soma de cada linha da matriz A.
Ao final apresentar o somatório dos elementos da lista B.
'''

matriz = []
listab = []


for lin in range (0,3):
    linha = []

    for col in range(0,3):
        linha.append(int(input("Digite os números inteiros da matriz")))
    matriz.append(linha)

for lin in range(0,3):
    print(matriz[lin])

##################################

for lin in range (0,3):
    somamariz = 0
    for col in range(0,3):
        somamariz = matriz[col]+somamariz
    listab.append(somamariz)

print(listab)