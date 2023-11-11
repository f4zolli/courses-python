"""
conversao de tipos, coercao
type convertion, typecasting, coercion,
eh o ato de converter um tipo em outro tipos iomutaveis e primitivos:
str, int, float, bool
"""
print('1', type('1')) # retorna 1 <class 'str'>, pois convertemos o 1 para string
print(int('1'), type('1')) # retorna 1 <class 'int'>, pois convertemos para int
print(int('1') + 1) # retorna 2, pois somou os dois numeros do tipo int
print(float('1') + 1) # retorna 2.0, pois somou um numero do tipo float com int
print(float('1.2') + 1) # retorna 2.2
print(bool(' ')) # retorna True