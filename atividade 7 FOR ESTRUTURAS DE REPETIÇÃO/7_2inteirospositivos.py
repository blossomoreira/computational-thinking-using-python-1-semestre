#Desenvolva um programa que receba um número inteiro positivo n.
# Exiba na tela a tabuada de multiplicação (0 ao 10) para o número informado pelo usuário.
# Conforme exemplo abaixo:

# Digite um número inteiro positivo: 5
#5 x 0=0
#5 x1 =5
#5 x2=10
#5 x3=15
#…
#5 x10=50
num = int(input("Digite o valor inteiro e positivo"))

for cont in range(1,11):
    tabuada = num * cont #pegamos o numero da contagem e transformamos em contadores para que sejam multiplicados com o numero


    print(tabuada)
