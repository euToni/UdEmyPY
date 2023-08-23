'''
Exercícios
Crie funções que duplicam, triplicam e quadruplicam 
o número recebico como parêmetro
'''

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4


# duplicarr = duplicar(29)
# print(duplicarr)




# def criar_multiplicador(multiplicador):
#     def multiplicar(numero):
#         return numero * multiplicador
#     return multiplicar

# duplicar = criar_multiplicador(2)
# triplicar = criar_multiplicador(3)
# quadruplicar = criar_multiplicador(4)

# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))

def multiplicar():
    n1 = input('Digite um numero: ')
    n1_inteiro = int(n1)
    
    return n1_inteiro * 2
print(multiplicar())