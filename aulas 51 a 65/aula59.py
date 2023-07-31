# Desempacotamento em chamadas
# de metódos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'Legal'

# a, b, *_, c = lista
# print(a, c)

print(*lista) # Passa todos os valores da lista com um espaço no sep=''
print(lista[0])