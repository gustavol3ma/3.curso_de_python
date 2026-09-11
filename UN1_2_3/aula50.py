'''

Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz

for in com listas
'''
lista = ['Maria','Helena','Luiz','Gustavo',123333]

i = 0
for nome in lista:
    print(i,nome, type(nome))
    i += 1

#Professor :

# lista = ['Maria', 'Helena', 'Luiz']
# lista.append('João')


# indices = range(len(lista))

# for indice in indices:
#     print(indice, lista[indice], type(lista[indice]))