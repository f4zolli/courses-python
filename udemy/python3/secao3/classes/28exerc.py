"""
Exercicio
Peca ao usuario para digitar seu nome
Peca ao usuario para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome eh {nome}
        Seu nome invertido eh {nome invertido}
        Seu nome contem (ou nao) espacos
        Seu nome tem {n} letras
        A primeira letra do seu nome eh {letra}
        A ultima letra do seu nome eh {letra}
Se nada fort digitado em nome ou idade:
    Exiba:
    "Desculpe, voce deixou campos vazios"
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome eh {nome}')
    print(f'Seu nome invertido eh {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu nome contem espacos')
    else:
        print('Seu nome NAO contem espacos')

    print(f'Seu nome tem {len(nome)} caracteres')
    print(f'A primeira letra do seu nome eh {nome[0]}')
    print(f'A ultima letra do seu nome eh {nome[-1]}')
else:
    print('Desculpe, voce deixou campos vazios')
