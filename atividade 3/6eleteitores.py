votos_nulos = int (input("Digite o total de votos nulos"))
votos_brancos = int (input("Digite o total de votos brancos"))
votos_validos = int (input("Digite o valor de votos validos"))

total_eleitores = votos_brancos + votos_nulos + votos_validos

percentual_votos_brancos = (votos_brancos * 100) / total_eleitores
percentual_votos_nulos = (votos_nulos * 100) / total_eleitores
percentual_votos_validos = (votos_validos * 100) / total_eleitores

print(f"O percentual de votos brancos foi: {percentual_votos_brancos: .2f}")
print(f"O percentual de votos nulos foi: {percentual_votos_nulos: .2f}%")
print(f"O percentual de votos validos foi: {percentual_votos_validos: .2f}%")