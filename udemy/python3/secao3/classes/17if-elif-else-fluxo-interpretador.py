# if / elif     / else
# se / se nao se/ se nao

condicao1 = False
condicao2 = False
condicao3 = True # se a condicao 4 fosse verdadeira, ela nao seria executada, visto que a 3 ja atendeu o bloco desse IF
condicao4 = False


if condicao1:
    print('Codigo para condicao1')
elif condicao2:
    print('Codigo para condicao 2')
elif condicao3:
    print('Codigo para condicao 3')
elif condicao4:
    print('Codigo para condicao 4')
else:
    print('Nenhuma condicao foi satisfeita')
