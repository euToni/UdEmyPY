entrada = input('[E]ntrar, [S]air: ')
senha_digitada = input('Senha: ')
senha = '123456'

if entrada == 'E' or entrada == 'e' and senha_digitada == senha:
    print('Entrar')
elif entrada == 'S' or entrada == 's':
    print('Sair')
else: 
    print('Senha incorreta.')