'''
Argumentos nomeados e não nomeados em funções python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''

def soma(x, y):
    # definição
    print(f'{x=} y={y}', '|', 'x + y =', x + y)

soma(50, 22)
soma(1, y=2)

print(1, 2, sep='-')