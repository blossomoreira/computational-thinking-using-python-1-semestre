'''
Faça um programa em Python que conte o número de 1’s
que aparecem em uma string. Exemplo: “0011001” = 3.
'''

string_numero = input('Digite seus numeros: ')
contador = 0

for qtde in string_numero:
    if qtde == '1':
        contador+=1

print(contador)