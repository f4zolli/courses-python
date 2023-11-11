a = 'A'
b = 'B'
c = 1.1
formato = 'a={} b={} c={}'.format(a, b, c) # dependendo da ordem das variaveis

print(formato)

# PRA ENTENDER MELHOR
string = 'a={0} b={1} c={2}' # pegando por indices (posicao da variavel), nao depende da ordem
formato = string.format(a, b, c)