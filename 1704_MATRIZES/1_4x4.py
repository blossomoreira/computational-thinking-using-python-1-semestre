matriz = []
nlin = 2
ncol = 2
maiores_dez = []

for lin in range (0,nlin):
    linha = [] #lista vazia para receber os elementos
    for col in range (0,ncol):
        elem = int(input("Digite um núemro inteiro aqui: "))
        linha.append(elem)

    matriz.append(linha)

    print(linha)





print(matriz)
