matriz = []

for lin in range (0,3):
    list = []
    for col in range (0,3):
        list.append(int (input('Digite os elementos da Matriz')))
    matriz.append(list)

for lin in range(0,3):
    print(matriz[lin])

maior = matriz[0][0]
maior_linha = 0
maior_col = 0

menor = matriz [0][0]
menor_linha = 0
menor_col = 0

for lin in range(0,3):
    for col in range(0,3):

        if (matriz[lin][col] > maior):
            maior = matriz[lin][col]
            maior_linha = lin
            maior_col = col
        if (matriz[lin][col] < menor):
            menor = matriz[lin][col]
            menor_linha = lin
            menor_col = col 


print(maior, maior_col, maior_linha)
print(menor, menor_col, menor_linha)