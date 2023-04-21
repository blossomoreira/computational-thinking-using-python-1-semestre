matriz = [] #aqui criamos a matriz vazia
nlin = 2 #num linhas
ncol = 2 #num olunas
maiores_dez = 0 #uma variável 0 para servir como contador

for lin in range (0,nlin):#for que faz as linhas
    linha = [] #lista vazia para receber os elementos
    for col in range (0,ncol): #for que faz as colunas
            linha.append(int(input("Digite números inteiros aqui: "))) 
    matriz.append(linha)

for lin in range (0,nlin):
    for col in range (0,ncol):
         if matriz[col][lin] > 10: #aqui pegamos os elementos dentro das matriz: matriz[col][lin]
              maiores_dez+=1
print(f"A quantidade de números inteiros maiores que dez são: {maiores_dez}")