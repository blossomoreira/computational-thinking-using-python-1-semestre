'''
Faça um programa que leia um número indeterminado de valores, 
correspondentes a notas, encerrando a entrada de dados quando for 
informado um valor igual a -1 (que não deve ser armazenado).

Após esta entrada de dados, faça: Mostre a quantidade de valores que 
foram lidos;
a. Calcule e mostre a soma dos valores;
b. Calcule e mostre a média dos valores;
c. Calcule e mostre a quantidade de valores acima da média calculada;
d. Calcule e mostre a quantidade de valores abaixo de sete.
'''
num = 0
lista = []
soma = 0
media = 0
qtde_media = 0
qtde_abaixo = 0
while num != -1:
    numeros_indeterminados = int(input('Digites os numeros: '))
    lista.append(numeros_indeterminados)

    media = 0
    qtde_media = 0
    qtde_abaixo = 0

print(lista)