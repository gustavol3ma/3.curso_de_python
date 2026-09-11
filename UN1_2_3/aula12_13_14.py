'''
#Introdução sobre formatação de strings
nome = 'Gustavo'
altura = 1.80
peso = 80
imc = peso / altura ** 2
print(nome, 'tem', altura,'de altura' )
print('Peso', peso, 'kg e seu IMC é de')
print(imc)

linha1 =f'{nome} tem altura de {altura:.2f}' #O .2f mostra quantas casa decimais você quer
linha2 =f'Peso{peso} kg e seu IMC é de{imc}'

print(linha1)
print(linha2)
'''
a = 'AAA'
b = 'Gustavo'
c = '111'
string1 = 'a = {1} b = {0} b = {1}'
string2 = 'a = {0} b = {1} b = {2}'
string3 = 'a = {0} b = {0} b = {1}'
formato1 = string1.format(a,b,c)
formato2 = string2.format(a,b,c)
formato3 = string3.format(a,b,c)

print(formato1)
print(formato2)
print(formato3)