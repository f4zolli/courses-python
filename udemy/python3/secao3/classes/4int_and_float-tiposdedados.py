# Tipos int e float
# int -> Numero inteiro
# O tipo int representa qualquer numero
# positivo ou negativo.
# int sem sinal eh considerado positivo

print (11) # int
print(-11) # int
print (0)

"""
float -> numero com ponto flutuante
o tipo float representa qualquer numero
positivo ou negativo com ponto flutuante
"""
print(1.1) # FLOAT, utiliza-se ponto para a quebra do numero e nao virgula.
print(0.0)
print(-1.5)

"""
a funcao TYPE (classe) mostra o tipo que o Python
inferiu ao valor
"""
print(type('Matheus')) # retorna <class 'str'>
print(type('1')) # retorna <class 'int'>
print(type('1.1')) # retorna <class 'float'>