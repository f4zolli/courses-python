"""
Repeticoes
while (enquanto)
Executa uma acao enquanto uma condicao for verdadeira
Loop infinito -> quando um codigo nao tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome? ')
    print(f'seu nome eh {nome}')

    if nome == 'sair':
        break # busca o while mais proximo
print('Acabou')