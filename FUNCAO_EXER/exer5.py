'''
Uma função que faça a leitura de uma lista com 10 números
inteiros como parâmetro e que retorne essa lista devidamente preenchida;
'''

def leituraDez(l):
    l = []
    for i in range(0,3):
        l.append(int(input('Digite os elementos')))
    print(l)
leituraDez(1)