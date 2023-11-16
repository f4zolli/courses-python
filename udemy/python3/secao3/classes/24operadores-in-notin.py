"""
Operadores IN(entre) e NOT IN(nao entre) 
Strings sao iteraveis
0 1 2 3 4 5 6
F a z o l l i
-7-6-5-4-3-2-1
"""

nome = 'Fazolli'
print(nome[2]) # para retorna a letra A do fAzolli
print(nome[-6]) # para retorna a letra A do fAzolli, de forma negativa
print('á' in nome) # para checar se a string 'á' esta entra a variavel NOME, retorna FALSE
print('z' in nome) # retorna TRUE

# EXEMPLO
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')

