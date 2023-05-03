'''
Faça um programa em Python que leia 10 números inteiros e armazene-os
 em uma lista. Em seguida, armazene os números pares na lista PAR e os 
números ÍMPARES na lista ímpar. Por fim, imprima as 3 listas.
'''
lista = [[],[]]
for i in range (10):
    num = int (input('Digite os elementos: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(lista)
print(lista[1])
print(lista[0])

        


    











