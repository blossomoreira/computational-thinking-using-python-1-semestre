'''
Um grupo de amigos resolveu fazer um happy hour em um bar
após o horário de trabalho. Na ocasião eles pediram porções de
batatas fritas, pastéis e cervejas para acompanhar.
Escreva um programa em Python que calcule o total do pedido baseado
nas quantidades de porções e cervejas consumidas tendo como referência
a tabela abaixo. Além disso, calcule o valor individual da conta de
acordo com o número de amigos.
'''

qtde_amigos = int(input('qtde amigos: '))

qtde_batata = 35 * float(input('Digite a qtde de porcoes de batata: '))
qtde_pastel = 25 * float(input('Digite a qtde de porcoes de pastel: '))
qtde_cerveja = 18 * float(input('Digite a qtde de porcoes de cerveja: ')) 

total_pedido = qtde_batata + qtde_cerveja + qtde_pastel
total_amigo =  total_pedido / qtde_amigos

print(total_pedido)
print(total_amigo)
