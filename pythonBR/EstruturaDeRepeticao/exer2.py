'''
Faça um programa que leia um nome de usuário e a sua senha
e não aceite a senha igual ao nome do usuário, mostrando
uma mensagem de erro e voltando a pedir as informações.
'''

while True:
    user_name = input('Username: ')
    password = input('Passoword: ')
    if user_name == password:
        print('The password and username can not be the same. Try something different.')
    else:
        break
print('Thank You!')
