#criar uma nova lista baseada no dobro dos elemntos de uma lista numérica com 5 valores

lista_a = [] #vazia pq usario vai digitar
lista_b = [] #lista nova para ser adiconado o dobro



#criação da lista a pelos dados do input
for i in range (5):
    num = int(input("Digite io nuemro"))
    lista_a.append(num)

#lista b dobro da lista a
for i in range (5):
    dobro = lista_a[i] * 2
    lista_b.append(dobro)

print(lista_a)
print(lista_b)