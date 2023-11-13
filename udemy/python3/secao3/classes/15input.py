# nome = input('Qual o seu nome?') # So funciona no terminal, pois ouput de editor de texto sao read only
# print(f'O seu nome eh {nome=}') # o = permite mostrar o nome da variavel no output

numero_1 = input('Digite um numero: ')
numero_2 = input('Digite outro numero: ')

# a melhor maneira de tratar caso o usuario inserisse uma letra no lugar do numero

int_numero_1 = int(numero_1) # convertendo (checando) a variavel para ser do tipo int
int_numero_2 = int(numero_2) # convertendo (checando) a variavel para ser do tipo int

print(f'A soma dos dois numeros eh: {int_numero_1 + int_numero_2}') # o resultado retorna a sona por conta do int() nas variaveis