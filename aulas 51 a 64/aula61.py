'''
O PRIMEIRO DIGITO DO CPF

CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF 
multiplicando cada um dos valores por uma contagem regressiva
começando de 10

Ex.: 746.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
*    7  4  6  8  2  4  8  9  0
    70 36 48 56 12 20 32 27  0

Somar todos os resultados:
    70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro digito do CPF é 7
'''
import os
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo = 10

resultado = 0
for digito in nove_digitos:
    print(f'{digito} X {contador_regressivo} = {int(digito) * contador_regressivo}')
    soma = int(digito) * contador_regressivo
    contador_regressivo -= 1
    resultado += soma
    print(resultado)
os.system('cls')

multiplicar_por_10 = resultado * 10
resto = multiplicar_por_10 % 11
novo_resto = resto if resto <= 10 else 0
print(novo_resto)
