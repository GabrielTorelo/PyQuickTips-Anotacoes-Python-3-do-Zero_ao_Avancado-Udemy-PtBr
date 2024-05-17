tuplas = (24, 'Gabriel', True, False, 1.80) # Tupla com vários tipos de dados

def imprime_argumentos(*args): # O *args é um parâmetro que permite que você passe um número variável de argumentos para uma função, convertendo-os em uma tupla
  for arg in args: # Para cada argumento em args
    print(arg)  # Imprima o argumento

imprime_argumentos(tuplas) # Como estou enviando uma tupla, o resultado será uma tupla
imprime_argumentos(24, 'Gabriel', True, False, 1.80) # Como estou enviando argumentos separados, o resultado será vários argumentos
