"""
Operador logico "not"
Usado para ivnerter expressoes
not True = False
not False = True
"""
senha = input('Senha: ')

if senha != '1234':
    print('Senha incorreta.')

if not senha:
    print('Voce nao digitou nada.')

# Exemplos
print(not True) # False
print(not False) # True


