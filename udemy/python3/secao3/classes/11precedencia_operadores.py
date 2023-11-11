# 1. (n + n) ele sempre executa os primeiros parenteses internos
# 2. ** potenciacao eh a segunda execucao
# 3. * / // % se tiver divisao e multiplicacao na mesma conta, executa da ESQUERDA p DIREITA
# 4. + -
conta_1 = 1 + 1 ** 5 + 5
print(conta_1) # retorna 7, pois ele fez a ordem dos comentarios acima