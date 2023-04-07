#Escreva um programa que faça a leitura das notas dos 3 checkpoints de 15 alunos
# e mostre a média dos checkpoints para cada aluno.



media_geral_aluno = 0

for alunos in range (15):

    nota1 = float(input("Digite a primeira nota"))
    nota2 = float(input("Digite a segunda nota"))
    nota3 = float(input("Digite a terceira nota"))

    media_geral_aluno = (nota1 + nota2 + nota3) / 3

    print(f"A média do seus checkpoints são: {media_geral_aluno: .2f}")