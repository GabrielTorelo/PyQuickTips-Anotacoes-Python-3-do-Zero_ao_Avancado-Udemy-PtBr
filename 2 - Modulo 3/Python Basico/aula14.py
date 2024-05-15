idade = '24'
idade = int(idade) # Pode gerar erro se a idade não for um número
print(f'Sua idade é {idade} anos')

# --------------------------------------------

ID_SERVIDOR = 123456
URL_SERVIDOR = 'https://www.servidor.com.br/id={}'.format(ID_SERVIDOR)

print(URL_SERVIDOR)

# --------------------------------------------

velocidade = 61 # km/h
km_carro = 98 # km onde o carro está

RADAR = 60 # km/h - Velocidade máxima permitida
LOCAL_RADAR = 100 # km - Local onde o radar está
RANGE_RADAR = 1 # km - Distância que o radar consegue captar

veloc_maior = velocidade > RADAR # 'True' se a velocidade for maior que a permitida
km_menor_radar = km_carro >= (LOCAL_RADAR - RANGE_RADAR)
km_maior_radar = km_carro <= (LOCAL_RADAR + RANGE_RADAR)
km_dentro_radar = km_menor_radar and km_maior_radar # 'True' se o carro estiver dentro do radar
carro_multado = veloc_maior and km_dentro_radar # 'True' se o carro foi multado

if carro_multado:
  print('\nVocê foi multado!')
else:
  print('\nVocê não foi multado!')
