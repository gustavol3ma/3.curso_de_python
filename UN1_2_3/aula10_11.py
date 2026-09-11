#concatenação de strings
print('-'*100)
print('Aula 10 - operadores')
concatenacao = 'Olá' + ' ' + 'Mundo'
print(concatenacao) 
concatenacao2 = 'Olá' + ' ' + 'Mundo' + str(204)
print(concatenacao2)
#repetição de string
repeticao = 'Olá' * 5
print(repeticao)

#1. ( n + n )
#2. **
#3. * / // %
#4. + -

print('-'*100)
print('Aula 11 - Precedência de operadores')
conta_1 = 1 + 1 * 5 + 5
print(conta_1)
conta_1 = (1 + 1) * (5 + 5)
print(conta_1)

print('-'*100)
print('Aula 12 - Calculo do IMC')
'''
 O IMC, é calculado dividindo o peso pela altura ao quadrado.
'''
Nome  =  'Camila'
peso = '58'
altura = '1.60'
imc = float(peso)/float(altura)**2 # O imc vai ser bom quando for menor que 18.5, normal entre 18.5 e 24.9, sobrepeso entre 25 e 29.9 e obesidade acima de 30
if imc < 18.5:
    print('Dados:')
    print('Nome:', Nome)
    print('Peso:', peso)
    print('Altura:', altura)
    print(f'{Nome} tem IMC de {imc:.2f} e está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Dados:')
    print('Nome:', Nome)
    print('Peso:', peso)
    print('Altura:', altura)
    print(f'{Nome} tem IMC de {imc:.2f} e está com peso normal')
elif 25 <= imc < 30:
    print('Dados:')
    print('Nome:', Nome)
    print('Peso:', peso)
    print('Altura:', altura)
    print(f'{Nome} tem IMC de {imc:.2f} e está com sobrepeso')
else:
    print('Dados:')
    print('Nome:', Nome)
    print('Peso:', peso)
    print('Altura:', altura)
    print(f'{Nome} tem IMC de {imc:.2f} e está com obesidade')
