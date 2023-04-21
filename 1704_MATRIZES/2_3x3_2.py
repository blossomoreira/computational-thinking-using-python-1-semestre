matriz = []

nlin = int(input("Digite o número de linhas da sua matriz"))
ncol = int(input("Digite o número de colunas da sua matriz"))

for lin in range(0,nlin):
    linha = []
    for col in range (0,ncol):
        linha.append(int (input('Digite os elementos de sua matriz')))
    matriz.append(linha)

for lin in range(0,nlin): #imprimindo matriz inteira
    print(matriz[lin])


k = int(input('Digite o valor de K'))
for lin in range (0, nlin):
    for col in range (0, ncol):
        if lin == col:
            matriz[col][lin] = matriz[col][lin] * k

for lin in range(0,nlin): #não esquecer de pegar a mesma linha
    print(matriz[lin])
