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

numero = input('Digite um numero inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    numero_par = numero_int % 2 == 0
    numero_par_texto = 'impar'

    if numero_par:
        numero_par_texto = 'par'
    
    print(f'O numero {numero_int} eh {numero_par_texto}')
else:
    print('Voce nao digitou um numero inteiro')

# exercicio 2

hora = input('Que hora eh agora? (digite em numeros inteiros): ')

try:
    entrada = int(hora)

    if entrada >= 0 and entrada <= 11:
        print(f'Bom dia, agora sao {entrada}hrs')
    elif entrada >= 12 and entrada <= 17:
        print(f'Boa tarde, agora sao {entrada}hrs')
    elif entrada >= 18 and entrada <= 23:
        print(f'Boa noite, agora sao {entrada}hrs')
    else:
        print('Nao existe 24hrs')

except:
    print('Voce nao digitou um numero inteiro')


nome = input('Insira seu primeiro nome: ')
contagem = len(nome)

if contagem <= 4:
    print('Seu nome eh curto')

if contagem == 5 or contagem == 6:
    print('Seu nome eh normal')

if contagem > 6:
    print('Seu nome eh mt grande')