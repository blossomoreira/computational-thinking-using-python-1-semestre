'''
Construa um programa em Python para preencher uma matriz,
de 6 linhas por 6 colunas, com elementos do tipo int.

Em seguida,o programa deve apresentar, na tela, todos os elementos
pares contidos na matriz, 
bem como a posição em que eles se encontram.
'''

matriz = []
for lin in range (0,3):
    linha = []
    for col in range (0,3):
        elementos = int(input('Digite seus elementos: '))
        linha.append(elementos)
    matriz.append(linha)

for lin in range (0,3):
    for col in range (0,3):
        if matriz[lin][col] % 2 == 0:
            print(f"({lin}, {col}): {matriz[lin][col]}")




    