#Escreva um algoritmo para ler 10 números.
# Todos os números lidos com valor inferior a 40 devem ser somados.
# Escreva o valor final da soma efetuada.

valor_inferior = 0

for i in range(3):

    num = int(input("Digite um valor"))

    if num < 40:

        valor_inferior = num + num

print(valor_inferior)

