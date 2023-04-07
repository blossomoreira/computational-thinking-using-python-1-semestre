#Escreva um programa que pergunte em qual mês estamos (1-12) e ao final utilize uma estrutura
# de decisão por seleção para escrever o nome do mês por extenso na tela.

mes_numero = int (input("Digite em que mes estamos"))

if mes_numero == 1:
    print("Janeiro")

elif mes_numero == 2:
    print("Fevereiro")

elif mes_numero == 3:
    print("Março")

elif mes_numero == 4:
    print("Abril")

elif mes_numero == 5:
    print("Maio")

elif mes_numero == 6:
    print("Junho")

elif mes_numero == 7:
    print("Julho")

elif mes_numero == 8:
    print("Agosto")

elif mes_numero == 9:
    print("Setembro")

elif mes_numero == 10:
    print("Outubro")

elif mes_numero == 11:
    print("Novembro")

elif mes_numero == 12:
    print("Dezembro")

else:
    print("Esse mÊs não existe")