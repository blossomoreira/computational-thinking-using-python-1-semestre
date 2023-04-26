'''
Elaborar um programa que efetue a leitura de 20 valores inteiros em
uma matriz A com 4 linhas e 5 colunas. Construir uma lista B para 4
elementos que seja formada pelo somatório dos elementos correspondentes
de cada linha da matriz A. Construir também uma lista C para 5 elementos
que seja formada pelo somatório dos elementos correspondentes de cada
coluna da matriz A. Ao final o programa deve apresentar os elementos
da lista B e da lista C.
'''

matrizA = []
listaB = []
listaC = []

for lin in range (0,3):
    linha = []
    for col in range (0,3):
        elementosA = int(input("Digite os elementos da Matriz A"))
        linha.append(elementosA)
    matrizA.append(linha)

for lin in range (0,3):    
    print(matrizA[lin])


for lin in range(0,3):
    somalinha = 0
    for col in range (0,3):
        somalinha = matrizA[lin][col]+somalinha
    listaB.append(somalinha)
print(listaB)

for lin in range(0,3):
    somacoluna = 0
    for col in range (0,3):
        somacoluna = matrizA[col][lin]+somacoluna
    listaC.append(somacoluna)       
print(listaC)
