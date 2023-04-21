#· Faça um programa que leia uma matriz 6x3 com números reais, calcule e mostre:
#(a) o maior elemento da matriz e sua respectiva posição (linha e coluna); 
#(b) o menor elemento da matriz e sua respectiva posição.

matriz = []

for lin in range (3):
    lista = []
    for col in range (3):
        lista.append(int (input("Digite os elementos da sua matriz aqui: ")))
    matriz.append(lista)

maior_numero = matriz[0][0]
maior_col = 0
maior_linha = 0

menor_numero = matriz[0][0]
menor_lin = 0
menor_col = 0

for lin in range (3):
    for col in range (3):
        if (matriz[lin][col]>maior_numero):
            maior_numero = matriz[lin][col]
            maior_linha = lin
            maior_col = col
        if (matriz[lin][col]<menor_numero):
            menor_numero = matriz[lin][col]
            menor_lin = lin
            menor_col = col

print(maior_numero, maior_linha, maior_col)
print(menor_numero,menor_lin, menor_col)



    



