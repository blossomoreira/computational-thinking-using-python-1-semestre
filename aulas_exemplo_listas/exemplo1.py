lista_numero = [2, 3, 4, 10, 70, 78]
# ______indice: 0  1  2  3  4  5  6 começa sempre por 0 e nós acessamos pelo indice
#vetor unidimencial: precisamos de apenas um valor
num = 78

#exibir um elemento da lista
#elementos da listas são os valores e nós podemos usar os inputs
print(lista_numero[0])

#saber qual indice o elemento está armazenado
print(lista_numero.index(10))

#exibe do primeiro elemento 0 até o 2
print(lista_numero[0:2])

#acessar elemntos dentro de um intervalo. terornar se um elemnto está na lista

if (num in lista_numero): #se num está dentro do lista numero print "o numero esta na lista"
    print("O numeor esta na lista")
else:
    print("o numero nao esta na lista")

#inserção d eum elemnto no final da lista

lista_numero.append(13)

print(lista_numero)


#outro metodo de inserção nos adiconamos um elemnto no indice de escolha. remanejando os elementos
#para poder inserir um novo

lista_numero.insert(4,18)

print(lista_numero)


#remoção de um elemnto da lista. duas formas

lista_numero.pop() #se quiser emover do indice só colocar o indice
print(lista_numero)


#dscobrir o tamanho da lista. metodo LEN

print("Tmanho da lista", (len(lista_numero)))


#tipos de dados heterogenios. listas com vrios tipos de dados. string, int e float(com casa dcimais)

lista_pessoa = ["Maria", 20, 1.56]



