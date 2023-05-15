'''
modularizar é dividir o projeto em partes menores
funcao começa com verbos (exibe, mostra)é uma ação
'''

def exibe_mensagem():
    print("Minha função")

exibe_mensagem()


def exibe_mensagem_custom (mensagem):
    print(mensagem)

#chamada da funcao

msg = "minha mensagem"

exibe_mensagem_custom(msg) #//nao posso 

############

def somando (num1,num2): #nao colocar funcao e var com o mesmo some
    soma = num1 + num2
    return(soma)

num1 = int(input("Digite o prokeor numero"))
num2 = int(input("Digite o segundo numero"))

#forma 1
s = somando (num1,num2)
print(s)


#forma2
print(somando (num1,num2))

######
def salculasoma_media(ini,fim):
    soma = 0
    cont_nuemrs = 0
    for i in range(ini,fim+1):
        soma+=i
        cont_nuemrs+=1
    media  = soma / cont_nuemrs
    return (soma,media)

ini = int(input("INI"))
fim = int(input("fimm"))

soma,media = salculasoma_media(ini,fim)

print(soma)
print(media)