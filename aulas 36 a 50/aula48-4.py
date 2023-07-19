'''
Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
'''

lista_a = ['luiz', 'maria']
lista_b = lista_a

lista_a[0] = 'qlqr coisa'
print(lista_b)