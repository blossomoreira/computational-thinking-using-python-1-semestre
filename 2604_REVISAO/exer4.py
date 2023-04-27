'''
Elaborar um programa em Python que efetue o cálculo de uma tabuada de um número qualquer e armazene os resultados em uma listaA
para 11 elementos. Apresentar os valores armazenados na lista.
'''

lista = []
for i in range (0,3):
    lista.append(int(input('Digite os numeros: '))*2)
print(lista)