'''
Faça um programa em Python que leia 10 números inteiros e armazene-os
 em uma lista. Em seguida, armazene os números pares na lista PAR e os 
números ÍMPARES na lista ímpar. Por fim, imprima as 3 listas.
'''

lista = [[],[]]
valor = 0

for i in range (0,10):
    valor = int(input('Digite os numeros: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(lista)

        


    











