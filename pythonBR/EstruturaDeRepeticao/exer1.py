'''
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido.
'''

while True:
    nota = int(input('Digite uma nota de 0 a 10: '))
    if nota < 0 or nota > 10:
        print('Valor inválido')
    else:
        break
print(f'Obrigado pela nota {nota}')
