matriz = []
contador_maiores = 0

for lin in range (0,3):
    linha = []
    for col in range (0,3):
        linha.append(int(input('Digite o valor dos elementos')))
    matriz.append(linha)

for lin in range (0,3):
    if matriz[lin][col] > 10:
        contador_maiores+=1
print(f"A matriz tem {contador_maiores} maiores que 10")