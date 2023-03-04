# Calcule e mostre a média aritmética tendo como base 4 avaliações (AV1,
# AV2, AV3 E AV4).

av1 = float (input("Digite a nota da Avaliação 1: "))
av2 = float (input("Digite a nota da Avaliação 2: "))
av3 = float (input("Digite a nota da Avaliação 3: "))
av4 = float (input("Digite a nota da Avaliação 4: "))

media = (av1 + av2 + av3 + av4) / 4

print(f"A sua média é: {media: .2f}")