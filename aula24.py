# nome = 'Angelo'

# print('An' in nome)
# print('gelo' in nome)
# print('A' not in nome)

nome = input('Nome: ')
encontrar = input('O que deseja encontrar? ')

if encontrar in nome: 
    print('{} está em {}'.format(encontrar, nome))
else:
    print('{} não está em {}'.format(encontrar, nome))