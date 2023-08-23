'''
Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

Crie uma função fala se um número é par ou ímpar 
Retorne se o número é par ou ímpar.
'''

        #Minha péssima tentaviva
# def multiplicar(*args):
#     for numero in args:
#         vezes = numero * args
#     return vezes

# resultado = multiplicar(2 * 5)
# print(resultado)

# def imparoupar():
#     if resultado % 2 == 0:
#         print('par')
#     else:
#         print('impar')
# imparoupar()
 

 # correção

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
resultado = multiplicar(3, 3,5 ,6 ,7 ,45, 23, 90)
print(resultado)

def imparoupar(saber):
    if saber % 2 == 0:
        print('Par')
    else:
        print('Ímpar')
imparoupar(resultado)
