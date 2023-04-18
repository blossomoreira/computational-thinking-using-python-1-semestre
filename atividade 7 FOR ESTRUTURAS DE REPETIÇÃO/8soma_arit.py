#Desenvolva um programa que receba 8 números inteiros positivos. Apresente a soma e média aritmética deles.

soma = 0
media = 0

for cont in range (1,4):
    num = float(input("Digite um número inteiro"))
    soma = soma + num
    media = soma / 3

print(soma)
print(media)



