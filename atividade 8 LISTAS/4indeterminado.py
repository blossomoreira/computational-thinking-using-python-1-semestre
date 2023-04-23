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

valores_lista = []
deseja = input('Deseja continuar: Digite (1) para SIM e (2) para NAO')
inputando = 0

while deseja == 1:
    if deseja == 1:
        inputando = input('Digite os valores')

