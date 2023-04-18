#Desenvolva um programa que receba:

#- taxa de abatimento em porcentagem;
#- número de prestações;
#- valor da primeira prestação.


#Seu programa deverá exibir na tela os valores das prestações decrescente dado que a cada mês
# o valor da prestação diminui do valor da prestação do mês anterior
# (utilize a taxa de abatimento fornecida pelo usuário para realizar esse cálculo).

#o valor da prestação diminui

cont = 1 #contador para reptoição no looping

taxa = float(input("Digite a taxa de abatimento: "))
nro_prest = int(input("Digite o numero de prestacoes: "))
valor_prim_prest = float(input("Digite o valor da primeira prestacao: "))

prest_abatimento = valor_prim_prest #a

while (cont <= nro_prest):

    prest_abatimento = prest_abatimento - (prest_abatimento * (taxa/100))
    print(f"Prestacao com abatimento: {prest_abatimento:.2f}")
    cont+=1