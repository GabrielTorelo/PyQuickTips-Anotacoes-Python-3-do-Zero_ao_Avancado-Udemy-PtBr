produto = {
  'nome': 'Lapis',
  'preco': 1.98,
  'categoria': 'Escolar',
}

dicionario = {
  chave: valor.upper() if isinstance(valor, str) else valor
  for chave, valor in produto.items()
}

print(dicionario)

# --------------------------------------------

print('\n')

# --------------------------------------------

lista = [
  ('a', 'valor a'),
  ('b', 'valor b'),
  ('c', 'valor c'),
]

dicionario = {
  chave: valor
  for chave, valor in lista
}

print(dicionario)
