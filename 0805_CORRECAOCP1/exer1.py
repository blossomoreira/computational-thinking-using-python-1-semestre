matrizA = []
listaB = []

for lin in range (0,3):
    linha = []
    for col in range (0,3):
        linha.append(int(input("Digite um elemnto da matriz: ")))
    matrizA.append(linha)
    print(matrizA)

for col in range(0,3):
    soma = 0
    for lin in range (0,3):
        if (col % 2 != 0):
            soma+=matrizA[lin][col]
    if (soma !=0):
        listaB.append(soma)


for lin in range(0,3):
    print(listaB)