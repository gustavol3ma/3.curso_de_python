"""
Interando strings com while
"""

#       0123456789....
nome = 'Gustavo Lima' 
#  print(nome[-11])

# tamanho_nome = len(nome)
# print(nome[1])
# print(tamanho_nome)

nv_nome = ''
i = 0
while i < len(nome):
    letra=nome[i] + '*'
    nv_nome += letra
    i += 1


print(nv_nome)