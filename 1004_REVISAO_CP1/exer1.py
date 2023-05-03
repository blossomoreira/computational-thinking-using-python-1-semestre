'''
Com a volta das aulas presenciais, a mãe de um aluno do ensino
fundamental necessita saber quanto gastará com material escolar.
Para fazer uma simulação, ela foi a uma livraria com o objetivo de
simular a compra dos seguintes itens básicos: canetas, lápis e cadernos.
Um ponto a se considerar é que essa livraria está com um programa de
desconto de 20% nos preços dos cadernos e 5% nas canetas. Assim sendo,
escreva um programa em Python que solicite as quantidades dos itens,
preços e calcule o total da compra simulada.
'''

qtde_canetas = int(input('Digite a qtde de canetas: '))
qtde_cadernos = int(input('Digite a qtde de cadernos: '))
qtde_lapis = int(input('Digite a qtde de lapis: '))


preco_canetas = float(input('Digite o preco das canetas: '))
preco_cadernos = float(input('Digite o preco das canetas: '))
preco_lapis = float(input('Digite o preco das canetas: '))

desc_caneta = preco_canetas * (20/100)
desc_cadernos = preco_cadernos - (5/100)

total_qtde = qtde_cadernos + qtde_canetas + qtde_lapis
total_preco = (preco_cadernos*qtde_cadernos) + (preco_canetas*qtde_canetas) + (preco_lapis*qtde_lapis)

print(total_preco)
print(total_qtde)

