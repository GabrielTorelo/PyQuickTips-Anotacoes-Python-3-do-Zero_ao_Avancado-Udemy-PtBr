"""
  1 - Crie uma função zipper (como o zipper de roupas)
    1.1 - O trabalho dessa função será unir duas listas na ordem.
    
    Use todos os valores da menor lista.
      Exemplo:
        lista 1: ['Salvador', 'Ubatuba', 'Belo Horizonte']
        lista 2: ['BA', 'SP', 'MG', 'RJ']

        Resultado
        lista 3: [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
"""

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

"""
  Função zipper
"""

def zipper(l1, l2):
  tam_min = min(len(l1), len(l2))

  return [
    (l1[i], l2[i]) for i in range(tam_min)
  ]

print(zipper(lista1, lista2))

# --------------------------------------------

print('\n')

# --------------------------------------------

"""
  Outras formas de resolver
"""

# --------------------------------------------
# ------------------- zip --------------------
# --------------------------------------------
print(list(zip(lista1, lista2))) # Usa todos os valores da menor lista

# --------------------------------------------
# --------------- zip_longest ----------------
# --------------------------------------------
from itertools import zip_longest

# Usa todos os valores da maior lista (preenche com 'Sem cidade' os valores faltantes)
print(list(zip_longest(lista1, lista2, fillvalue='Sem cidade')))
