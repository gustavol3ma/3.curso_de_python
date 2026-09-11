# Variáveis
# Variáveis são usadas para armazenar valores e dados em um programa. Elas permitem que você armazene informações e as utilize posteriormente no código.
# Em Python, você pode criar uma variável simplesmente atribuindo um valor a ela usando o operador de atribuição (=). O nome da variável deve seguir algumas regras, como começar com uma letra ou um sublinhado, e não pode conter espaços ou caracteres especiais.
# Exemplo de criação de variáveis       
nome = "Gustavo Lima"
idade = 25
altura = 1.75
é_estudante = True

nome_completo = "Gustavo Silva Lima" #variável com nome composto, usando underscore para separar as palavras
print(nome)
soma_dois_numeros = 10+10
bool_um = bool('1') #qualquer string não vazia é considerada True, e qualquer string vazia é considerada False
print(bool_um)
bool_zero = bool('0') #Aqui o valor '0' é uma string não vazia, então é considerado True. Se fosse o número 0, seria considerado False.
print(bool_zero)

nome = "Gustavo Lima"
idade = 25
altura = 1.75
é_estudante = True
maior_de_idade = idade >= 18
print('=================================================================================')

#Atividade
nome = "Gustavo Lima"
sobrenome = 'Silva'
Idade  =  25
Ano_de_nascimento = 2026 - Idade
E_maior_de_idade = Idade >= 18
Altura_em_metros = 1.75
print('=================================================================================')  
print('Nome:',nome)
print('=================================================================================')  
print('Sobrenome:',sobrenome)
print('=================================================================================')  
print('Idade:',Idade)
print('=================================================================================')  
print('Ano de nascimento:', Ano_de_nascimento)
print('=================================================================================')  
print('É maior de idade?', E_maior_de_idade)
print('=================================================================================')  
print('Altura em metros:', Altura_em_metros)