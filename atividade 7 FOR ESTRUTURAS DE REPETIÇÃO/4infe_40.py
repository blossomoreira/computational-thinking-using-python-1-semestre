# Escreva um algoritmo para ler 10 números. Todos os números lidos com valor inferior a 40 devem ser somados.
# Escreva o valor final da soma efetuada.

soma = 0

for i in range (4):
    num = int(input("Digite o número: "))
    if num < 40:
        soma = num + num
print(soma)

