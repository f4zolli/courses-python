# Mostrar quando um valor eh maior que o outro (no meu caso, coloquei se fosse igual tb)

valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')

if valor1 > valor2:
    print(f'O primeiro valor ({valor1}) eh maior do que o segundo valor ({valor2})')
elif valor1 == valor2:
    print(f'O primeiro valor ({valor1}) eh igual o segundo valor ({valor2})')
else:
    print(f'O segundo valor ({valor2}) eh maior do que o primeiro valor ({valor1})')