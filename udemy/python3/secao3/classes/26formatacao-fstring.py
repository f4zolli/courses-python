"""
Formatacao basica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ouj -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # preenche com 10 espacos da esquerda para a direita
print(f'{variavel: <10}') # preenche com 10 espacos da direita para a esquerda
print(f'{variavel: ^10}') # coloca o ABC no meio da linha
print(f'{1000.4324234324234:.1f}') # o 1 indica a quantidade de casas decimais que vc deseja que exiba
print(f'O hexadecima de 1500 eh {1500:08X}') #Casa decimal
print(f'{variavel!r}') # metodo __repr__ 