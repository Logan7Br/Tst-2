numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    if  numero_int % 2 == 0:
        print(f'O numero {numero} é par')

    else:
        print('O número não é par')

except:
    print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom Dia 0-11, Boa Tarde 12-17 e Boa Noite 18-23.
"""
dia = input ('Digite a hora: ')
numero_int = int(dia)

MEIO_DIA = 6
TARDE = 15
NOITE = 19
DIA_RANGER1 = 1 
DIA_RANGER2 = 2
DIA_RANGER3 = 3
DIA_RANGER4 = 4
DIA_RANGER5 = 5
DIA_RANGER6 = 6

manha = numero_int >= (MEIO_DIA - DIA_RANGER6) and \
   numero_int <= (MEIO_DIA + DIA_RANGER5)

tarde = numero_int >= (TARDE - DIA_RANGER3) and \
   numero_int <= (TARDE + DIA_RANGER2)

noite = numero_int >= (NOITE - DIA_RANGER1) and \
   numero_int <= (NOITE + DIA_RANGER4)


if manha:
   print('Bom dia')

if tarde:
   print('Boa tarde')

if noite:
   print('Boa Noite')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
nome = input('Digite seu nome: ')
quantidade = len(nome)

if quantidade <= 4:
    print('Seu nome é curto')

elif quantidade <= 6:
    print('Seu nome é normal')


else:
    print('Seu nome é muito grande')
