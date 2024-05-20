"""
  Crie uma função que encontra o primeiro duplicado considerando o segundo
  número como a duplicação.
  Retorne a duplicação considerada.

  Requisitos:
    1 - A ordem do número duplicado é considerada a partir da segunda
      ocorrência do número, ou seja, o número duplicado em si.
      Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    2 - Se não encontrar duplicados na lista, retorne -1
"""

lista_de_listas_de_inteiros = [
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], # Não tem duplicados (-1)
  [9, 1, 8, 9, 9, 7, 2, 1, 6, 8], # 9 é o primeiro duplicado
  [1, 3, 2, 2, 8, 6, 5, 9, 6, 7], # 2 é o primeiro duplicado
  [3, 8, 2, 8, 6, 7, 7, 3, 1, 9], # 8 é o primeiro duplicado
  [4, 8, 8, 8, 5, 1, 10, 3, 1, 7], # 8 é o primeiro duplicado
  [1, 3, 7, 2, 2, 1, 5, 1, 9, 9], # 2 é o primeiro duplicado
  [10, 2, 2, 1, 3, 5, 10, 5, 10, 1], # 2 é o primeiro duplicado
  [1, 6, 1, 5, 1, 1, 1, 4, 7, 3], # 1 é o primeiro duplicado
  [1, 3, 7, 1, 10, 5, 9, 2, 5, 7], # 1 é o primeiro duplicado
  [4, 7, 6, 5, 2, 9, 2, 1, 2, 1], # 2 é o primeiro duplicado
  [5, 3, 1, 8, 5, 7, 1, 8, 8, 7], # 5 é o primeiro duplicado
  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], # Não tem duplicados (-1)
]

def encontra_duplicado(lista_de_inteiros: list) -> int: # Função que encontra o primeiro duplicado
  numeros_unicos = set() # Conjunto de números únicos

  for numero in lista_de_inteiros: # Percorre a lista de inteiros
    if numero in numeros_unicos: # Se o número já existe no conjunto
      return numero # Retorna o número duplicado
    
    numeros_unicos.add(numero) # Adiciona o número ao conjunto
  return -1 # Se não encontrar duplicados, retorna -1

for lista_de_inteiros in lista_de_listas_de_inteiros: # Percorre a lista de listas de inteiros
  print(encontra_duplicado(lista_de_inteiros)) # Imprime o primeiro duplicado encontrado de cada lista de inteiros
