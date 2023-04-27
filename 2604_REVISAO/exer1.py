'''
Escreva um programa em Python para ler uma lista A com 10 elementos
numéricos inteiros.

Apresentar o total de elementos ímpares existentes
na lista
e o percentual do valor total de números ímpares em relação à
quantidade total de elementos armazenados na lista
'''

listaA = []
contador = 0

for i in range (0,3):
    numeros = int(input('Digite os numeros: '))
    listaA.append(numeros)

for i in listaA:
    if i % 2 != 0:
        contador+=1
        
percentual = (contador / len(listaA)) * 100

print(contador, percentual)