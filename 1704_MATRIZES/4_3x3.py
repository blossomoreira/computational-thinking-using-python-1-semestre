#· Faça um programa que leia uma matriz 3x3 de inteiros e 
#retorne a linha de maior soma. Imprima na tela a matriz, 
#a linha de maior soma e a soma.

matriz = []

for lin in range (0,3):
    linha = []
    for col in range(0,3):
        linha.append(int(input('Digite os elemntos da matriz: ')))
    matriz.append(linha)
for lin in range (0,3):
    print(matriz[lin])
print('\n')



for lin in range(0,3):
    soma_linhas = 0
    for col in range(0,3):
        soma_linhas+=matriz[lin][col] #da 24 por ser o ultimo valor que a var contou



    if (lin==0):
        maior = soma_linhas #aqui criamos uma var para coloca a soma das linhas
        lin_maior = 0 #uma var zerada para receber os valores
    else:
        if