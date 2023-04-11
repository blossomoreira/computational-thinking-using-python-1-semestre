qtde_maiorigualsete = 0
lista_media = []

for i in range (10):
    check1 = float(input("a"))
    check2 = float(input("b"))
    check3 = float(input("c"))

    media = (check1 + check2 + check3) / 3
    lista_media.append(media)

for i in range (10):
    if (lista_media[i] >= 7.0):
        qtde_maiorigualsete+=1

print(f"fodoes que ganharam 7 {qtde_maiorigualsete}")