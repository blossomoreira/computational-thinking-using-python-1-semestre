#Mostrar todos os inteiros entre dois números digitados pelo usuário.
# Exemplo: usuário digita os números 8 e 15, e aparecem em tela: 9, 10, 11, 12, 13, 14.


num1 = int(input("Digite num1: "))
num2 = int(input("Digite o num2: "))

cont = num1 + 1 #aqui estamos fazendo uma var fora do loop para poder contar para o valor já ser atribuido automaticamnete

while (cont < fim):
    print(cont) #aqui damos print primeiro
    cont+=1 #aqui adicionamos mais um valor para que ele possa contar novamente até chgar no num2
