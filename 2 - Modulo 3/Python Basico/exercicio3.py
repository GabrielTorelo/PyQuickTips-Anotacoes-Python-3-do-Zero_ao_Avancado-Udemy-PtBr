"""
  Ler a entrada de dois números e imprimir qual é o maior.
"""

primeiro_valor = input('Digite o primeiro número: ')

if primeiro_valor.isnumeric():
  primeiro_valor = int(primeiro_valor)
else:
  print('O primeiro valor inserido deve ser um número.')
  exit()

segundo_valor = input('Digite o segundo número: ')

if segundo_valor.isnumeric():
  segundo_valor = int(segundo_valor)
else:
  print('O segundo valor inserido deve ser um número.')
  exit()

if primeiro_valor > segundo_valor:
  print(f'O {primeiro_valor=} é maior do que {segundo_valor=}.')
else:
  print(f'O {segundo_valor=} é maior do que {primeiro_valor=}.')
  