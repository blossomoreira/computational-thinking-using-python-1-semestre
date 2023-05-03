'''
O custo de um carro novo ao consumidor é a soma do custo de
fábrica com a porcentagem do distribuidor e dos impostos
(aplicados ao custo de fábrica). Supondo que o percentual do
distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo
para ler o custo de fábrica de um carro, calcular e escrever o
custo final ao consumidor.
'''

custo_fabrica = float(int(input('Qual custo de fabrica? ')))
custo_carro_novo = custo_fabrica + (custo_fabrica * (45/100)) + (custo_fabrica * (28/100))

print(f'{custo_carro_novo:.2f}')