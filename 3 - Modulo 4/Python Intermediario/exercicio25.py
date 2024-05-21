"""
  Considerando duas listas de inteiros ou floats (lista A e lista B)
    1 - Some os valores nas listas retornando uma nova lista com os valores somados:
      Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

  Exemplo:
    lista_a = [1, 2, 3, 4, 5, 6, 7]
    lista_b = [1, 2, 3, 4]

    lista_soma  = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# Cria a função para somar as listas
def soma_listas(lista1, lista2):
  tam_min = min(len(lista1), len(lista2)) # Pega o tamanho da menor lista

  return [
    lista1[i] + lista2[i] for i in range(tam_min) # Soma os valores das listas
  ]

print(soma_listas(lista_a, lista_b))

"""
  Outras formas de resolver
"""

# --------------------------------------------
# ------------------- zip --------------------
# --------------------------------------------

lista_c = list(
  map(sum, zip(lista_a, lista_b))
)

print(lista_c)

# --------------------------------------------
# ---------------- map & zip -----------------
# --------------------------------------------

lista_d = [
  x + y
  for x, y in zip(lista_a, lista_b)
]

print(lista_d)
