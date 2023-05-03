lista_notas = []
soma_notas = 0
qtde_acimamedia = 0
qtde_abaixosete = 0

nota = float(input("Digite a nota: "))

while (nota != -1):
    soma_notas += nota
    lista_notas.append(nota)
    nota = float(input("Digite a nota: "))

qtde_notas = len(lista_notas)
media_notas = soma_notas / qtde_notas

for i in range (qtde_notas):
    if (lista_notas[i] > media_notas):
        qtde_acimamedia+=1
    if (lista_notas[i] < 7.0):
        qtde_abaixosete+=1

print(f"Soma das notas: {soma_notas:.2f}")
print(f"Media das notas: {media_notas:.2f}")
print(f"Quantidade de notas acima da média calculada: {qtde_acimamedia}")
print(f"Quantidade de notas abaixo de sete:{qtde_abaixosete}")


