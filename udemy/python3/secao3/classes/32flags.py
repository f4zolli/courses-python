"""
Flag (Bandeira) - Marcar um local
None = Nao valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

condicao = False
passou_no_if = None # se eu colocar um valor nulo na variavel, ela nao gerara erro caso o codigo nao passe por onde ela foi definida

if condicao:
    passou_no_if = True # a variavel foi definida aqui, porem nao foi passada para TRUE, logo, o valor continua como NONE
    print('Faca algo')
else:
    print('Nao faca algo')

print(passou_no_if, passou_no_if is None) # CONDICAO para verificar a se variavel ainda continua como NONE, retorna NONE TRUE
print(passou_no_if, passou_no_if is not None) # CONDICAO para verificar se a variavel nao eh igual a NONE, retorna NONE FALSE, pois a variavel eh TRUE

if passou_no_if is None:
    print('Nao passou no if')
else :
    print('Passou no if')

# ou
if passou_no_if is not None:
    print('Passou no if')