'''
O gerente de um bar precisa fazer um levantamento do movimento
no final do expediente. Basicamente, o bar oferece um menu (tabela abaixo)
onde cada item tem um código associado. Considerando que ele tem uma
relação das comandas com as quantidades consumidas por mesa, escreva
um programa em Python faça a leitura do código e da quantidade de cada
item até que o usuário digite 0 (1-continuar e 0-parar).

Calcule o total para cada comanda baseado nas quantidades
de porções e cervejas consumidas e o valor total geral do dia.
Para tanto, utilize a estrutura de repetição “while”.
'''

inicializador = int(input('DESEJA INICIAR? (01) CONTINUAR - (00) PARAR'))

C01 = 35.00 # P/ FRITAS
C02 = 25.00 # P/ PASTEIS
C03 = 40.00 # TABUA FRIOS
C04 = 55.00 # P/ PEIXES
C05 = 18.00 # CERVEJA

while inicializador == 1:
    qtdeC01 = int(input('Digite a quantidade porcoes de fritas (C01): '))
    qtdeC02 = int(input('Digite a quantidade porcoes de pasteis (C02): '))
    qtdeC03 = int(input('Digite a quantidade de tabua frios (C03): '))
    qtdeC04 = int(input('Digite a quantidade porcoes de peixes (C04): '))
    qtdeC05 = int(input('Digite a quantidade de cervejas (C05): '))

    total = (C01 * qtdeC01) + (C02 * qtdeC02) + (C03 * qtdeC03) + (C04 * qtdeC04) + (C05 * qtdeC05)
    print(total) 
    inicializador = int(input('(01) CONTINUAR - (00) PARAR'))


