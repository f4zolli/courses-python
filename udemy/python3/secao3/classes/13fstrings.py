# OBSERVACAO O 'f' na variavel resposta permite inserir variaveis em uma string
# o :.2f eh a formatacao da quantidade de numeros que eu quero de um numero do tipo float

nome = 'Matheus Fazolli'
altura = 1.80
peso = 94
imc = peso / (altura ** 2)

resposta = f'{nome} tem {altura:.2f} de altura pesa {peso} quilos e seu IMC é {imc:.2f}'

print(resposta)

# Matheus Fazolli tem 1.80 de altura,
# pesa 94 quilos e seu IMC é
# valor IMC