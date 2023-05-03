
soma = 0
num = int(input("Digite um numero: "))

while (num >= 0):
    soma = soma + num  # soma+=num
    num = int(input("Digite um numero: "))

print(f"Soma dos positivos: {soma}")