'''
Escreva um programa em Python que dada uma string com uma frase
informada pelo usuário (incluindo espaços em branco), conte quantos
espaços em branco existem na frase.
'''

esapco = " "

string = input("Digite uma string: ")
contador = 0

for letra in string:
    if letra in esapco:
        contador += 1

print(f"A string '{string}' possui {contador} espaços em branco.")