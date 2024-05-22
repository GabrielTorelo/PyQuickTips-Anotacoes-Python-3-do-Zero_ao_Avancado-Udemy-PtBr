from functools import *

produtos = [
  {'nome': 'Produto 5', 'preco': 10.00},
  {'nome': 'Produto 1', 'preco': 22.32},
  {'nome': 'Produto 3', 'preco': 10.11},
  {'nome': 'Produto 2', 'preco': 105.87},
  {'nome': 'Produto 4', 'preco': 69.90},
]

precos_produtos = [
  prod['preco']
  for prod in produtos
]

# --------------------------------------------
# ------------- Métodos nativos --------------
# --------------------------------------------

aumenta_preco = \
  list(
    map(
      lambda prod: round(prod * 1.05, 2),
      precos_produtos
    )
  )

print(aumenta_preco)

filtra_produtos = \
  list(
    filter(
      lambda prod: prod % 2 == 0,
      precos_produtos
    )
  )

print(filtra_produtos)

# --------------------------------------------
# --------- Métodos do 'functools' -----------
# --------------------------------------------

reduz_produtos = \
  reduce(
    lambda atual, prox: round(atual + prox, 2),
    precos_produtos
  )

print(reduz_produtos)

def multiplicar(x, y):
  return x * y

multiplicar_por_2 = partial(multiplicar, 2)

print(multiplicar_por_2(5))
