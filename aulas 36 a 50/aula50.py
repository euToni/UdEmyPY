'''
Exercício
Exiba os índices da lista

'''

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

indices = range(len(lista))

for itens in indices:
    print(itens, lista[itens])