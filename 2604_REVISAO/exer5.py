'''
Escreva um programa em Python para ler 12 elementos inteiros para uma
lista A.

Construir uma lista B de mesmo tipo e dimensão,
observando a seguinte lei de formação:


"Todo elemento da lista A que for ímpar deve ser multiplicado por 2;
caso contrário, o elemento da lista A deve permanecer constante".
Apresentar a lista B.
'''

listaA = []
listaB = []

for i in range (0,3):
    elementos = int(input('Digite seus elementos da lista A: '))
    if elementos % 2 != 0:
        elementos *=2
    listaB.append(elementos)

for i in range (0,3):
    elementos = int(input('Digite seus elementos da lista B: '))



print(listaB)
print(listaA)