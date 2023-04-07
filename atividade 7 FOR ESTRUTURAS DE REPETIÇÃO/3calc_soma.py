#•	Escreva um programa que calcule a soma de todos os números pares entre 1 e 20.

soma_pares = 0 #aqui estamos criando uma var para poder colocar o valor dos pares

for i in range (21): #aqui estamos falando que a contagem vai ser até 0 20

    if (i % 2 == 0): #se o resto da divisão dos numeros i forem 0, é um número par
        soma_pares = soma_pares + i #então vamos pegar esses valores e somar com todos

print(soma_pares)

