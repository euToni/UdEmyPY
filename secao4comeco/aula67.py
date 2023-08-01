'''
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será usado.

Default Values for parameters
When defining a function, the parameters can have default values. If the value is not sent to the parameter, the default value is gonna be used

Refatorar o código == Editar
'''

def soma(x, y, z=None):
    if z is not None: 
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=} =', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)