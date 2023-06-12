'''
Repetições 
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
'''

condicao = True

while condicao:
    nome = input('Qual é o seu nome? ')
    print(f'Seu nome é {nome}')
    print('-'*20)

    if nome == 'Sair':
        break

print('Acabou')