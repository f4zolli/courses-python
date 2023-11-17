"""
Interpolacao basica de Strings
s - string
d e i - int
f - float
x e x - hexadecimal (ABCDEF0123456789)
"""
nome = 'Matheus'
preco = 1000.95897643
variavel = '%s, o preco eh R$%.2f' % (nome, preco) # colocamos em parenteses pois sao duas variaveis no mesmo local
print(variavel)
print('O hexadecial de %d eh %04x' % (15, 15)) # 04x eh a quantidade de casa decimais que vc quer utilizar