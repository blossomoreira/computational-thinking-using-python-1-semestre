numeroum = float (input("Digite o primeiro numero"))
numerodois = float (input("Digite o segundo numero"))

opc = int (input("Digite a opção que você quer"))

match opc:
    case 1:
        valor_soma = numeroum + numerodois
        print(valor_soma)

    case 2:
        valor_sub = numeroum - numerodois
        print(valor_sub)
    case 3:
        valor_mult = numeroum * numerodois
        print(valor_mult)

    case 4:
        valor_div = numeroum / numerodois
        print(valor_div)

