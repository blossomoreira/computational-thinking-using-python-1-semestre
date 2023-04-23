'''
Faça um programa em Python que peça as 3 notas de 10 alunos, 
calcule e armazene em uma lista a média de cada aluno. 
Em seguida, imprima o número de alunos com média maior ou igual a 7.0.
'''

lista_media = []
calc = 0
qtde_notas = 0

for alunos in range (3):
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    calc = (nota1 + nota2 + nota3) / 3
    lista_media.append(calc)
print(lista_media)

if calc >= 7:
    qtde_notas+=1
print(f'um total de {qtde_notas} tiraram mais que 7.0')
