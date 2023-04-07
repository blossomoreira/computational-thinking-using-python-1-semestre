#•	As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00
# se forem compradas pelo menos 12. Escreva um programa
# que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

quantidade_macas = float (input("Quantas maacas voce comprou"))

valor_macas = quantidade_macas * 1.30

if quantidade_macas < 12:
    print(f"O valor a pagar é {valor_macas: .2f}")

else:
    print(f"O valor a pagar é: {quantidade_macas: .2f}")