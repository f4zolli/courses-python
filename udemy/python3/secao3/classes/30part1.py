"""
CONSTANTE = "variaveis" que nao vao mudar, normalmente no python eh indicada com LETRAS MAIUSCULAS
Muitas condicoes no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 50 # velocidade atual do carro
local_carro = 100 # local em que o carro esta na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGE = 1 # a distancia onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('Velocidade do carro passou da velocidade permitida do radar 1')

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if  carro_multado_radar_1:
    print('Carro foi multado no radar 1')