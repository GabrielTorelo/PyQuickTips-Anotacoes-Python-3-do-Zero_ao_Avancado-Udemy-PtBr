pessoa = {
  'nome': 'Aline',
  'sobrenome': 'Souza',
}

dados_pessoa = {
  'idade': 16,
  'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}

print(pessoas_completa)

# --------------------------------------------

print('\n')

# --------------------------------------------

def mostrar_args(*args, **kwargs):
  print('Args não nomeados: ', *args, sep=' | ', end=' | \n\n')

  for chave, valor in kwargs.items():
    print(f'{chave}: {valor}')

dict_args = {
  'arg1': 1,
  'arg2': 2,
  'arg3': 3,
  'arg4': 4,
}

mostrar_args(1, 2, 3, 4, **dict_args)
