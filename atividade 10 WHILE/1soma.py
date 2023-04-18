#Somar todos os números inteiros de 1 a N, em que N é um número inteiro digitado pelo usuário.
# Exemplo: usuário digita o valor de N igual a 5, então soma = 1 + 2 + 3 + 4 + 5 = 15.

number = int (input("Digite o valor de N")) #Aqui colocamos o valor de N
cont = 1 #Aqui temos um contatdor para contar de 1 em 1 durante o while
soma = 0 #Um avr para guardar a soma fora do looping

while cont <= number: #enquanto o cont for menor ou igual number, vamos fazer o looping para chegar no número do number
    soma = soma + cont #aqui usamos a var soma zerada para guardar o cont e a própia soma
    cont = cont + 1 #aqui o cont está guardando o cont mais 1 até que cont seja menor ou igual o número
print(soma)