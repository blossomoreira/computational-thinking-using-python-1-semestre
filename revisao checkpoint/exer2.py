qtde_porcoes_batas = int(input("Digite a quantidade de porções de batatas"))
qtde_porcoes_pasteis = int(input("Digite a quantidade de porções de pasteis"))
qtde_porcoes_cervejas = int(input("Digite a quantidade de porções de cervejas"))

qtde_amigos = int(input("Qauntos amigos vão rachar?"))

valor_total = (qtde_porcoes_batas * 35.00) + (qtde_porcoes_pasteis * 25.00) + (qtde_porcoes_cervejas * 18.00)

valor_racha = valor_total / qtde_amigos

print(f"cada amigo devera pagar {valor_racha: .2f}")

