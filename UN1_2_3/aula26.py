# Formatação básica de strings

# s - string
# d - int
# f - float

# .<número de dígitos>f
# x ou X - Hexadecimal
# (Caractere) (><^) (quantidade)
# > - Esquerda
# < - Direita 
# ^ - Centro
# Sinal - + ou -
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a

var = 'ABC'
print(f'{var}')
print(f'{var: >10}') #vai preencher 10 caracteres a esquerda
print(f'{var: <10}') #vai preencher 10 caracteres a direita 
print(f'{var: ^10}') #vai preencher 10 caracteres no centro (Aqui usei espaço em branco, mas você pode usar outras coisas)
