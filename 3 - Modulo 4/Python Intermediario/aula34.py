# Criando lista com diversos tipos de dados
lista = [
  'a',1, 1.1, True, [0, 1, 2], (1, 2),
  {0, 1}, {'nome': 'Luiz'}
]

# Percorrendo a lista e verificando o tipo de cada item
for item in lista:
  if isinstance(item, set): # Verifica se o item é do tipo set
    print(f'"{item}" é do tipo "set"!')
  elif isinstance(item, str): # Verifica se o item é do tipo string
    print(f'"{item}" é do tipo "string"!')
  elif isinstance(item, bool): # Verifica se o item é do tipo bool
    print(f'"{item}" é do tipo "bool"!')
  elif isinstance(item, (int, float)): # Verifica se o item é do tipo int ou float
    print(f'"{item}" é do tipo "numb"!')
  else: # Caso não seja nenhum dos tipos acima
    print(f'"{item}" é de um tipo não mapeado!')
