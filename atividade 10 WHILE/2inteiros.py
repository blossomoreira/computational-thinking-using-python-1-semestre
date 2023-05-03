#Mostrar todos os inteiros entre dois números digitados pelo usuário.
# Exemplo: usuário digita os números 8 e 15, e aparecem em tela: 9, 10, 11, 12, 13, 14.

num1 = int(input('Digite numero 1'))
num2 = int(input('Digite numero 2'))
contador = 0
contador+=num1

while contador < num2:
    contador+=1
    print(contador)