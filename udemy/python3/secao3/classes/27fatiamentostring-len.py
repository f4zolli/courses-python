"""
Fatiamento de strings
 012345678
 Ola mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a funcao len retorna a quantidade de caracteres da string
"""

variavel = 'Ola mundo'
print(variavel[5]) # retorna letra U, podendo utilizar tambem o -4
print(variavel[4:7]) # retorna MUN, pois pega o primeiro indicie (4) e UM indice atras do 7 (que setamos como final)
print(variavel[4:8]) # caso quisessemos que retornasse o D, ou seja, MUND
print(variavel[4:]) # omite ate o final da string, ou seja, MUNDO
print(variavel[0:4]) # retorna "Ola m"
print(variavel[-8:-2]) # retorna "la mun"
print(len(variavel[3])) # len retorna 1 (quantidade de caractere que tem no espaco indicado)
print(len(variavel)) # len retorna 9 (quantidade de caracteres da variavel)
print(variavel[0:len(variavel):1]) # retorna "Ola mundo", pois Iniciou do indice 0, contou 9 (qtd de caracteres) e de 1 em 1 passo
print(variavel[0:9:2]) # retorna "Oamno" pois foi setado de 2 em 2 passos.
print(variavel[-1:-10:-1]) # inverte da direita para a esquerda os passos, retorna "odnum alO"