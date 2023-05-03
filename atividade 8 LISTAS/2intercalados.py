'''
Faça um programa em Python que leia duas listas com 10 elementos cada.
Gere uma terceira lista de 20 elementos, cujos valores deverão ser
compostos pelos elementos intercalados das 2 listas.
'''

lista1 = []
lista2 = []
lista3 = []

for i in range (3):
    lista1.append(int(input('valores lista 1')))
    lista2.append(int(input('valores lista 2')))

for i in range(3):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista1)
print(lista2)
print(lista3)