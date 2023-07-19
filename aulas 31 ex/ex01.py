"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""


# ------------------MINHA SOLUÇÃO------------

# n1 = input('Digite um número inteiro: ')
# n1_float = float(n1)

# if n1_float // 1 == n1_float:
#     print(f'O número {n1_float:-6f} é inteiro')
# else:
#     print('Número decimal')

# if n1_float % 2 == 0:
#     print('O número digitado é par')
# else:
#     print('O número digitado é ímpar')


# -------------CORREÇÃO----------------------

entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'


    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')

