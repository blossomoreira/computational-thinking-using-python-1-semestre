custo_fabrica = float (input("Digite o custo de fábrica do veiculo"))

percent_distri = custo_fabrica * 0.28

percent_imposto = custo_fabrica * 0.45

custo_final = custo_fabrica + percent_imposto + percent_distri

print(f"CUSTO FINAL É {custo_final: .2f}")