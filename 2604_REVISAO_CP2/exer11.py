'''
Crie um programa que recebe uma string e um caractere digitado
pelo usuário e retorne o número de vezes que esse caractere aparece
na string.
'''

string_palavra = input('Digite a palavra: ')
caractere = input('Digite o caracter: ')
contador = 0

for caracteres in string_palavra:
    if caracteres == caractere:
        contador+=1
print(f'O caracter {caractere} aparece {contador} vezes na palavra {string_palavra}')