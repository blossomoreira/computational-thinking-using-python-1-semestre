# lista criada a partir do input

#declaramos uma lista vazia primeiro

lista = []

for i in range(10): # varia de 0 a 9 (0 é um numero tambem)
    nome = input("Digite o nome")
    lista.append(nome)

for i in range (10): #range já em na vertical então por isso um por um. meu contatdor é o indice da lista
    print(lista[i])

for nome in lista: #aqui ela trasnforma tudo em string (nome) e imrpime os nomes
    print(lista) ##!!!!!!!!!!!!!!! deu errado