'''
Escreva um programa em Python para ler uma matriz 3X6 de números reais.
Em seguida, quando houver números negativos, troque-os pelo número 1.
Por fim, mostre a matriz atualizada.
'''

matriz = []
for lin in range (0,3):
    linha = []
    for col in range (0,3):
        elementos = int (input('Digite os elementos: '))
        if elementos < 0:
            elementos=1
        linha.append(elementos)
    matriz.append(linha)

for lin in range(0,3):
    print(matriz[lin])
    
