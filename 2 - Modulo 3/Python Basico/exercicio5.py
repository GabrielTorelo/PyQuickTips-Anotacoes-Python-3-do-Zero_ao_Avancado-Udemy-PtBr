"""
  Ler uma entrada de dado e caso não seja um número gerar uma exceção
"""

try:
  idade = input('Digite a sua idade: ')
  idade = int(idade)
  print(f'Sua idade é {idade} anos')
except:
  print(f'Idade informada "{idade}" é inválida!')
