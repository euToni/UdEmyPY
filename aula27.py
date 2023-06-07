# EXERCICIO

nome = input('Qual é o seu nome? ')
idade = input('Quantos anos você tem? ' )

if nome and idade != '':
    print('Seu nome é {}'.format(nome))
    print('Seu nome invertido é: {}'.format(nome[::-1]))
else:
    print('Preencha os campos anteriores para obter os resultados.')

if ' ' in nome:
    print('Seu nome contém espaços!')
else:
    print('Não contém espaços')

print('Seu nome tem {} letras!'.format(len(nome)))
print('A  primeira letra do seu nome é {}. A última letra do seu nome é {}'.format(nome[0], nome[-1]))
