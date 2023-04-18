#substituindo elementos

matriz = []

nlin = 3
ncol = 3

for lin in range (0,nlin): #3 linhas
    linha = [] #o for lin vai passar pos aqui
    for col in range (0,ncol):# 4 coluna
        elem = int(input("Digite ume elemento da linha" +str(lin+1)+ ": " )) #insere os elementos na linha (na sublista)
        linha.append(elem) #coloca o elemento na linha
    matriz.append(linha) #insere uma linha na matriz
