#Escreva um programa que pergunte ao usuário qual foi a média anual de um aluno
# e ao final diga se ele está aprovado, reprovado ou de exame.
# Considere que o aluno está aprovado caso a média seja maior
# ou igual a 6.0; de exame com a média entre 3.0 e 5.9 e reprovado com média menor do que 3.0.

media_anual = float (input("Qual media anual do aluno?"))

if media_anual >= 6.0:
    print("Aprovado")

elif media_anual >= 3.0:
    print("Exame")

else:
    print("Reprovado")