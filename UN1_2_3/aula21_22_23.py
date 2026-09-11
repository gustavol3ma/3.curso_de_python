#Operadores lógicos 
# and (e) or (ou) not (não)
#and - Todas as condições precisam ser verdadeiras.
#Se qualquer valor for considerado falso,a expressão inteira será avaliada naquele valor 
#São considerados falsy 
#0 0.0 '' False
#Também existe o tipo None que é 
# Usado para representar um não valor  


# entrada = input('[E]ntrar  [S]air : ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'
 
# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

#Avaliação de curto circuito 

# print(True and True and True)
# print(True or False)
# print(True or False or 0)
# print(False or False or 0 or 'abc')

# senha = input('Senha: ') or 'Sem Senha'
# print(senha)

#Operador lógico 'not'
# Usado para inverter expressões 
# not True = False 
# not False = True 

senha = input('Senha: ')

if not senha :
    print('Você não digitou nada ')
