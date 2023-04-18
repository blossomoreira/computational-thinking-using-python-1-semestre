#Escreva um programa que receba números inteiros positivos até que um número menor igual a 0 seja digitado.
# Ao final mostre o maior e o menor dentre os números digitados.

num = int(input("Digite um numero: ")) #aqui colocamos o inpu
cont = 1 #aqui temos u contador para o laço funcionar

while (num > 0): #enquanto o numero digitado for maior que 0, o laço irá funccionar. se ele for 0 irá parar

    if (cont==1): #o cont for maior igual a 1 9que é), essa condição irá armanezar os números.
        maior = num
        menor = num

    else: #n entendi mt bem o else aqui já que a condição sempre é verdadeira, pq isso está rolando.

        if (num > maior):
            maior = num
        if (num < menor):
            menor = num

    cont+=1## pq tem um contador aqui?????

    num = int(input("Digite um numero: "))


print(f"Maior: {maior}")
print(f"Menor: {menor}")