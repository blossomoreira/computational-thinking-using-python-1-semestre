num = int (input("Digite um número"))
num_adicional = int (input("Digite um número para adicionar a lista"))
lista_numeros = [num, 18, 3, 15]

if (num in lista_numeros):
    print("O numeor esta na lista")
    print(lista_numeros.index(num))
else:
    lista_numeros.append(num_adicional)
    print("Agora o número está na lista")
    

