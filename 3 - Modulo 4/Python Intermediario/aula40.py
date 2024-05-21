from itertools import *

cores = ['vermelho', 'verde', 'azul']

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = ['a', 'b']

alunos = [
  {'nome': 'Luiz', 'nota': 'A'},
  {'nome': 'Letícia', 'nota': 'B'},
  {'nome': 'Marcos', 'nota': 'A'},
  {'nome': 'Rosemary', 'nota': 'C'},
  {'nome': 'Joana', 'nota': 'D'},
  {'nome': 'João', 'nota': 'A'},
  {'nome': 'Eduardo', 'nota': 'B'},
  {'nome': 'André', 'nota': 'A'},
  {'nome': 'Anderson', 'nota': 'C'},
]

# --------------------------------------------
# ----------- Iteradores Infinitos -----------
# --------------------------------------------

for i in count(1):
  if i == 11:
    break

  print(f"Entrou pela {i}ª vez")

print()

ciclo_cores = cycle(cores)

for i in range(6):
  print(f'{i + 1}:', next(ciclo_cores))

print()

for item in repeat('Python', 3):
  print(item)

print()

# --------------------------------------------
# --------- Iteradores Combinatórios ---------
# --------------------------------------------

print(list(product(lista1, lista2)), end='\n\n')

print(list(combinations(lista1, 2)), end='\n\n')

print(list(permutations(lista1, 2)), end='\n\n')

# --------------------------------------------
# ------ Iteradores Entrada Mais Curta -------
# --------------------------------------------

print(list(accumulate(lista1)), end='\n')

def ordena(aluno):
  return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
  print(f'\nNota {chave}', end=': ')
  
  for aluno in grupo:
    print(aluno['nome'], end=', ')

print('\n')

print(list(dropwhile(lambda x: x < 5, lista1)), end='\n\n')

print(list(takewhile(lambda x: x < 5, lista1)), end='\n\n')

print(list(zip_longest(lista1, lista2, fillvalue='Não existe')))
