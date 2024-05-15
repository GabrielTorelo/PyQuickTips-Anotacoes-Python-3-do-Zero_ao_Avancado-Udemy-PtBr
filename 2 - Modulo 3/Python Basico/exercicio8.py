"""
  Criar uma calculadora que realiza as 4 operações básicas (soma, subtração, multiplicação e divisão) com while.
"""

numeros = []
i = 0

while True:
  i += 1

  try:
    user_input = input(f'Insira o {i}º número: ')
    numeros.append(float(user_input))
  except ValueError:
    print('\nInsira apenas números.')
    exit()
  
  if i == 2:
    break

operation = input('\nQual a operação deseja? [S]oma, [M]ultiplicação, [D]ivisão, [Sub]tração: ').lower()

if operation == 's':
  result = sum(numeros)
  print(f'\nO resultado da soma é: {result}')
elif operation == 'm':
  result = numeros[0] * numeros[1]
  print(f'\nO resultado da multiplicação é: {result}')
elif operation == 'd':
  result = numeros[0] / numeros[1]
  print(f'\nO resultado da divisão é: {result}')
elif operation == 'sub':
  result = numeros[0] - numeros[1]
  print(f'\nO resultado da subtração é: {result}')
else:
  print('\nOperação inválida.')

# Versão usando funções:
#
# numeros = []
# i = 0
#
# def soma(numeros):
#   return sum(numeros)
#
# def subtracao(numeros):
#   result = numeros[0]
#
#   for num in numeros[1:]:
#     result -= num
#
#   return result
#
# def multiplicacao(numeros):
#   result = numeros[0]
#
#   for num in numeros[1:]:
#     result *= num
#
#   return result
#
# def divisao(numeros):
#   result = numeros[0]
#
#   for num in numeros[1:]:
#     result /= num
#
#   return result
#
# while True:
#   i += 1
#
#   try:
#     user_input = input(f'Insira o {i}º número: ')
#     numeros.append(float(user_input))
#   except ValueError:
#     print('\nInsira apenas números.')
#     exit()
#
#   if i >= 2:
#     while True:
#       resp = input('Deseja inserir mais um número? [S/N]: ')
#       if resp.lower() == 's' or resp.lower() == 'n':
#         break
#       else:
#         print('Resposta inválida.')
#         continue
#
#     if resp.lower() == 'n':
#       break
#
# operation = input('\nQual a operação deseja? [S]oma, [M]ultiplicação, [D]ivisão, [Sub]tração: ').lower()
#
# if operation == 's':
#   result = sum(numeros)
#   print(f'\nO resultado da soma é: {result}')
# elif operation == 'm':
#   result = multiplicacao(numeros)
#   print(f'\nO resultado da multiplicação é: {result}')
# elif operation == 'd':
#   result = divisao(numeros)
#   print(f'\nO resultado da divisão é: {result}')
# elif operation == 'sub':
#   result = subtracao(numeros)
#   print(f'\nO resultado da subtração é: {result}')
# else:
#   print('\nOperação inválida.')
