resp = 1

total = 0

while (resp != 0):
    print("postção de fritas")
    print("postção de pasteis")
    print("postção de frios")
    print("postção de porcao de peixes")
    print("postção de cervejas")

    cod_produto = int(input("digite coidgo"))
    qtde_produto = int(input("Digite a quantidade do produto: "))

    resp = int(input("Seseka continuar? 1sim  - 0nao"))

    match cod_produto:
        case 1:
            subtotal = qtde_produto * 35.00
            total = total + subtotal

        case 2:
            subtotal = qtde_produto * 25.00
            total = total + subtotal

        case 3:
            subtotal = qtde_produto * 45.00
            total = total + subtotal

        case 4:
            subtotal = qtde_produto * 55.00
            total = total + subtotal
        case 5:
            subtotal = qtde_produto * 18.00
            total = total + subtotal
        case _:
            print (int("codigo invalido"))
    resp - int(input("Digite se quer continuar"))