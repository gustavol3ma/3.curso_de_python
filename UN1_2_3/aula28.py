'''
Exercício 
Peça ao usuário para digitar seu nome 
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é ...
        Seu nome invertido é .....
        Se nome contém (ou não) espaços
        Seu nome tem n letras 
        A primeira letra do seu nome é ...
        A última letra do seu nome é ...
se nada for digitado em nome ou idade:
    exiba "Desculpe", você deixou campos vazios
'''

#variaveis 
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if nome and idade != '':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')


    if ' ' in nome:
        print('Nome contém espaço')
    else:
        print('Nome não contém espaço')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

else:
    print('"Desculpe", você deixou campos vazios')
