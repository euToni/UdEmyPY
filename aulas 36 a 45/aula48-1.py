"""
Listas em python
Tipo list - Mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
 append, insert, pop, del. clear, extend, +
 Create Read Update   Delete
 Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40, 'eu']
lista[2] = 300
del lista[2]

print(lista)
lista.append(50)
lista.pop() # -> deleta o ultimo item da lista
lista.append(60) # -> add coisas ao final da lista
lista.append(70)
print(lista)
print(lista[2])

