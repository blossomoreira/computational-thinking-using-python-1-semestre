'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

while True:
    idade = int(input('Digite sua idade: '))
    if idade < 0 or idade > 150:
        print('Idade inválido.')
    else:
        break
print('Idade válida')

###########################
while True:
    nome = input('Digite seu nome: ')
    if len(nome) < 3:
        print('Nome inválido.')
    else:
        break
print('Idade válida')

print(f'seu nome é {nome} e sua idade é {idade}')