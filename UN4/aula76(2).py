# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}
#quantas chaves 
print(pessoa.__len__) 
print(len(pessoa))

#quantas chaves 
print(tuple(pessoa.keys()))
for chaves in pessoa.keys():
    print(chaves)
    
#iterável com os valores
for valor in pessoa.values():
    print(valor)

#iterável com chaves e valores
for chave, valor in pessoa.items():
      print(chave, valor)

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))




#PARTE 2 DA AULA 


pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}
