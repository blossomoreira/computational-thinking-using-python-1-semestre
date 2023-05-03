'''
Faça um programa em Python que peça as 3 notas de 10 alunos, 
calcule e armazene em uma lista a média de cada aluno. 
Em seguida, imprima o número de alunos com média maior ou igual a 7.0.
'''

listanotas = []
calc = 0
cont = 0
for i in range (3):
    cp1 = float(input('Digite a nota do CP1: '))
    cp2 = float(input('Digite a nota do CP2: '))
    cp3 = float(input('Digite a nota do CP3: '))
    calc = (cp1+cp2+cp3) / 3
    listanotas.append(calc)
    print(listanotas)
    if calc >= 7.0:
        cont+=1
print(cont)
