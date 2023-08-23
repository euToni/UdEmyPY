'''
Introdução às funções (def) em python
Funções são trechos de código usados para replicar
determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
'''

# def ola():
#     print('Oi')
#     print('Td')
#     print('Bem')
#     print('Com')
#     print('vc?')
# ola()

def imprimir(nome='Geraldo'):
    print(f'Olá, {nome}!')

imprimir(input('Qual é o seu nome? '))
imprimir()

