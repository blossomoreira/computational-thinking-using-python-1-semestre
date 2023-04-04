num = float (input("Digite o numero inteiro real"))

opc = int(input("Digite o valor que você quer"))

match opc:

    case 1:
        num = num + 5
        print(num) #aqui imrpime o resultado do match, por isso precisa colocar aqui dentro do match


    case 2:
        num = num - 4
        print(num)

    case 3:
        num = 2 * num
        print(num)
