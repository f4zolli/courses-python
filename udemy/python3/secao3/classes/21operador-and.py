'''
Operadores lógicos
and (e), or (ou), not(nao)
and - Todas as condicoes precisam ser verdadeiras.
Se qualquer valor for considerado falso, a expressão inteira será
avaliada naquele valor.
São considerados falsy (que vc ja viu) 0, 0.0, '', False
Também existe o tipo None que é usado para representar um não valor 
'''

entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')


senha_permitida = '1234'
# if condicao: if soh eh executado quando toda expressao eh True!
# isso se chama AVALIACAO DE CURTO CIRCUITO
if entrada == 'E' and senha == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print(entrada)
