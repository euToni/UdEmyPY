'''
Retorno de valores das funções (return)
'''

def soma(x, y):
    if x > 10:
        return 10
    return x + y

# Existem dois tipos de função   
# 1- Funções que apenas executam ações e não retornam nada;
# 2- Funções que são especificas para retornar valores

# variavel = soma(1,2)
# variavel = int('1')
# print(variavel)

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)