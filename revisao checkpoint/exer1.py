preco_caneta =  float(input("Digite o preco da caneta"))
preco_lapis =  float(input("Digite o preco da lapis"))
preco_caderno =  float(input("Digite o preco da caderno"))

qtde_caneta = float(input("Digite a quantidade de cametas"))
qtde_lapis = float(input("Digite a quantidade de cametas"))
qtde_caneta = float(input("Digite a quantidade de cametas"))

preco_caderno_desc = preco_caderno - (preco_caderno * (20/100))
preco_caneta_desc = preco_caneta - (preco_caneta * (5/100))

valor_total = (qtde_caneta * preco_caneta_desc) + (qtde_lapis * preco_lapis)