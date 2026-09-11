#Exercício 01 

# num1 = input('Digite um número inteiro: ')

# if num1:
#     num1_int = int((num1))
#     impar_par = num1_int % 2 == 0
#     impar_par_texto = 'Ímpar'

#     if impar_par:
#         impar_par_texto = 'Par'

#     print(f'O número {num1_int} é {impar_par_texto}')
     

# else:
#     print('Você não digitou um número inteiro')

# #Agora usando try e except

# num2 =  input('Digite um segundo número inteiro: ')

# try:
#     num2_int = int(num2)
#     par_impar =  num2_int%2 == 0
#     text_par_impar = 'Ímpar'

#     if par_impar:
#         text_par_impar = 'Par'
    
#     print(f'O número {num2_int} é {text_par_impar}')
    
# except:
#     print('Você não digitou um número inteiro')

#Exercício 02 
# Bom Dia   -> 0-11
# Boa Tarde -> 12-17
# Boa Noite -> 18-23 

# entrada = input('Digite a Hora (Digite em número inteiro): ')

# try:
#     entrada_int = int(entrada)

#     if  entrada_int>= 0 and entrada_int<=11:
#         print('BOM DIA!!!')
#     elif entrada_int>= 12 and entrada_int<=17:
#         print('BOA TARDE!!!')
#     elif entrada_int>= 18 and entrada_int<=23:
#         print('BOA NOITE!!!!')
# except:
#     print('Você digitou errado!!!')
    
# entrada = input('Digite a Hora: ')

# try:
#     hora = float(entrada)

#     if 0 <= hora < 12:
#         print('BOM DIA!!!')
#     elif 12 <= hora < 18:
#         print('BOA TARDE!!!')
#     elif 18 <= hora < 24:
#         print('BOA NOITE!!!')
#     else:
#         print('Hora inválida!')
# except ValueError:
#     print('Você digitou um valor inválido!')

#Exercício 03

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


entrada = input('Digite seu primeiro nome: ')
contador_nome = len(entrada)


if contador_nome<=4:
    print("Seu nome é curto")

elif contador_nome<=5 and contador_nome <=6:
    print("Seu nome é normal")

elif contador_nome>6:
    print("Seu nome é muito grande")