def leituraDez():
    l = []
    soma = 0
    for i in range(0,3):
        l.append(int(input('Digite os elementos')))
        soma+=i
        media=soma/3
        print(soma,media)
leituraDez()

