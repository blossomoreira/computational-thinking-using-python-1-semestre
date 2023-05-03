qtde_maiorigualsete = 0
lista_medias = []

for i in range (10):
    check1 = float(input("Digite a nota do checkpoint 1: "))
    check2 = float(input("Digite a nota do checkpoint 2: "))
    check3 = float(input("Digite a nota do checkpoint 3: "))
    media = (check1 + check2 + check3) / 3
    lista_medias.append(media)

for i in range (10):
    if (lista_medias[i] >= 7.0):
        qtde_maiorigualsete+=1

print(lista_medias)
print(f"Quantidade de alunos com media maior ou igual a sete: {qtde_maiorigualsete}")