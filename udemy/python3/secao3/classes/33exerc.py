"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

numero = int(input('Digite um numero inteiro: '))

if numero % 2 == 0:
    print('O numero que voce digitou eh par')
else:
    print('O numero que vc digitou eh impar')

if int(numero):
    print('O numero eh do tipo inteiro')
else:
    print('O numero NAO eh do tipo inteiro')

# exercicio 2

hora = int(input('Que hora eh agora? '))

bom_dia = hora <= 11
boa_tarde = hora >= 12 and hora <= 17
boa_noite = hora >= 18 and hora <= 23

if bom_dia:
    print(f'Bom dia, agora eh {hora}hrs')

if boa_tarde:
    print(f'Boa tarde, agora eh {hora}hrs')

if boa_noite:
    print(f'Boa noite, agora eh {hora}hrs')


nome = input('Insira seu primeiro nome: ')
contagem = len(nome)

if contagem <= 4:
    print('Seu nome eh curto')

if contagem == 5 or contagem == 6:
    print('Seu nome eh normal')

if contagem > 6:
    print('Seu nome eh mt grande')