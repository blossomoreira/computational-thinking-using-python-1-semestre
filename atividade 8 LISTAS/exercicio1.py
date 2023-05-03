lista_numeros = []
lista_pares = []
lista_impares = []

for i in range (10):
    num = int(input("Digite um numero: "))
    lista_numeros.append(num)

for i in range (10):
    if (lista_numeros[i] % 2 == 0):
        lista_pares.append(lista_numeros[i])
    else:
        lista_impares.append(lista_numeros[i])

print(lista_numeros)
print(lista_pares)
print(lista_impares)
