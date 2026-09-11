'''
Faça uma lista de compra com listas 
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não é permita que o programa quebre com 
erros de índices inexistente na lista
'''
#Minha solução 
# print('Selecione uma opção')
# lista = []

# while True:
#     item = input('[i]inserir, [a]apagar, [l]listar : ').lower()

#     if item == 'i':
#         valor = input('Digite o item: ')
#         lista.append(valor)
#         continue

#     if item == 'a':
#         if len(lista) == 0:
#             print('A lista está vazia!!!')
#             continue
            
#         valor_apagado = input('Digite o nome exato do item para apagar: ')
        
#         if valor_apagado in lista:
#             lista.remove(valor_apagado)
#             print(f'Item "{valor_apagado}" apagado com sucesso!')
#         else:
#             print('O item não está na lista!!!')
#         continue

#     if item == 'l':
#         if len(lista) == 0:
#             print('Nada para listar. A lista está vazia.')
#             continue
            
        
#         print('\n---LISTA DE COMPRAS ---')
#         for indice, nome in enumerate(lista):
#             print(f'{indice} - {nome}')
#         print('----------------------------')

#Solução do Professor 

import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
