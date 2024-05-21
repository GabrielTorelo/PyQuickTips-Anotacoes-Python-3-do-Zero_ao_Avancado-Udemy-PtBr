import copy
from packages import produtos

"""
  1 - Aumente os preços dos produtos a seguir em 10%
  2 - Gere novos_produtos por deep copy (cópia profunda)
"""

# Aumenta o preço dos produtos em 10%
novos_produtos = [
  {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
  for produto in copy.deepcopy(produtos) # A cópia profunda é feita com a função copy.deepcopy
]

# Imprime os produtos com o preço aumentado
for produto in novos_produtos:
  print(produto)

# --------------------------------------------

print('\n')

# --------------------------------------------

"""
  3 - Ordene os produtos por nome decrescente (do maior para menor)
  4 - Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
"""

# Ordena a lista de produtos pelo nome
produtos_ordenados_por_nome = \
  sorted( # A '\' serve para quebrar a linha
    copy.deepcopy(produtos), # A cópia profunda é feita com a função copy.deepcopy
    key=lambda produto: produto['nome'], 
    reverse=True
  )

# Imprime os produtos ordenados pelo nome
for produto in produtos_ordenados_por_nome:
  print(produto)

# --------------------------------------------

print('\n')

# --------------------------------------------

"""
  5 - Ordene os produtos por preco crescente (do menor para maior)
  6 - Gere produtos_ordenados_por_preco por deep copy (cópia profunda)  
"""

# Ordena a lista de produtos pelo preço
produtos_ordenados_por_preco = \
  sorted( # A '\' serve para quebrar a linha
    copy.deepcopy(produtos), # A cópia profunda é feita com a função copy.deepcopy
    key=lambda produto: produto['preco']
  )

# Imprime os produtos ordenados pelo preço
for produto in produtos_ordenados_por_preco:
  print(produto)
