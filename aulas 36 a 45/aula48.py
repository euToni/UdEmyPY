"""
Listas em python
Tipo list - Mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del. clear, extend, +
"""

#        +01234      
#        -54321     
string = 'ABCDE' # 5 caracteres (len)
# print(bool([])) # falsy, Uma lista vazia retorna false

lista = [123, True, 'Antônio', 1.2, []]
lista[2] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
