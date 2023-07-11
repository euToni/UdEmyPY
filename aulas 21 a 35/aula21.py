# OPERADORES LÓGICOS.... and, or, not

imput = input('Digite [E] para entrar ou [S] para sair. ')
senha_d = input('Senha: ')
senha = '123456'


if imput == 'E' and senha_d == senha:
    print('Entrou')
elif imput == 'S' or senha_d != senha:
    print('Saiu')
else:
    print('Leia novamente e faça o que se pede')