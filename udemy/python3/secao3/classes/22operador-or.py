'''
Operadores lógicos
and (e), or (ou), not(nao)
or - Qualquer condicao verdadeira avalia toda a expressao como verdadeira.
Se qualquer valor for considerado verdadeiro, a expressao inteira
sera avaliada naquele valor.
Sao considerados falsy (que vc ja viu) 0, 0.0, '', False
Tambem existe o tipo None que eh usado para representar um valor NAO VALOR 
'''
entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')


senha_permitida = '1234'
# CUIDADO COM EXPRESSAO AMBIGUA (QUANDO TIVER OR E AND NA MESMA EXPRESSAO)
if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print(entrada)

# AVALIACAO DE CURTO CIRCUITO

senha_curto = input('Senha: ') or 'Sem senha' # Caso a pessoa nao insira o input, mostra que o campo esta sem senha
