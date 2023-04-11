num = [[],[]]
valor = 0

for cont in range (10):
    valor = int(input("Digite um numero"))

    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f"LISTA PAR: {num[0]} e LISTA IMPAR {num[1]}")



        


    











