'''
Calculo do segundo dígito do CPF
CPF = 746.824.890-70
Colete a soma dos 9 primeiro dígitos do CPF, MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma contagem regressiva começando de 11

Ex.:    746.824.890-70(7468248907)
    11 10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0  7  <--Primeiro Digito
    77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado == 0
else:
    resultado == valor da conta

O segundo dígito do CPF é 0
'''

import os
import string


cpf = '070.549.191-90'
cpf_sem_ponto = cpf.translate(str.maketrans('', '', string.punctuation))
nove_digitos = cpf_sem_ponto[:9]
contador_regressivo_1 = 10

resultado = 0
for digito in nove_digitos:
    print(f'{digito} X {contador_regressivo_1} = {int(digito) * contador_regressivo_1}')
    soma = int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
    resultado += soma
    print(resultado)

multiplicar_por_10 = resultado * 10
resto = multiplicar_por_10 % 11
novo_resto = resto if resto < 10 else 0
print(novo_resto)

dez_digitos = nove_digitos + str(novo_resto)
contador_regressivo_2 = 11

resultado_1 = 0
for digito_1 in dez_digitos:
    print(f'{digito_1} X {contador_regressivo_2} = {int(digito_1) * contador_regressivo_2}')
    soma_1 = int(digito_1) * contador_regressivo_2
    contador_regressivo_2 -= 1
    resultado_1 += soma_1

multiplicar_por_10_dnovo = resultado_1 * 10
resto_1 = multiplicar_por_10_dnovo % 11
resto_1 = resto_1 if resto_1 <= 9 else 0

os.system('cls')

d1, d2 = novo_resto, resto_1
print(f'Os Finais do CPF são {d1, d2}')
tres_p = cpf_sem_ponto[:3]
tres_m = cpf_sem_ponto[3:6]
tres_u = cpf_sem_ponto[6:9]
print(f'O CPF é: {tres_p}.{tres_m}.{tres_u}-{d1}{d2}')

novo_cpf = f'{nove_digitos}{d1}{d2}'

descobrir = input('Quer descobrir se o cpf é válido ou não? [s]im [n]ão: ')

if descobrir == 's' or descobrir == 'S':
    print('Ok')
    if novo_cpf == cpf_sem_ponto:
        print('O CPF é válido')
    else:
        print('O CPF é inválido :/ ')
elif descobrir == 'n' or descobrir == 'N':
    
    print('OK')
else:
    print('Apenas [s] ou [n]')
