"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

"""

numero_str = input('Vou dobrar o número que vc digitar: ')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2}')
# else:
#     print('Isso não é um número')

# isdigit() -> verifica se o usuário digitou somente numeros obs(APENAS números) logo números com vírgula não são aceitos e retornam false

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:2}')
except:
    print('Isso não é um número')