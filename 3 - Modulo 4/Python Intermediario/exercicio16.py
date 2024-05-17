"""
  Crie uma função que multiplique todos os argumentos não nomeados recebidos
    * Retorne o total para uma variável e mostre o valor da variável.
"""

numeros = (1, 2, 3, 4, 5) # Cria uma tupla com os números '1, 2, 3, 4 e 5'

def multiplica_argumentos(*args): # O *args é um parâmetro que permite que você passe um número variável de argumentos para uma função, convertendo-os em uma tupla
  total = 1 # Inicializa a variável total com 1, pois a multiplicação de qualquer número por 1 é o próprio número

  for arg in args: # Para cada argumento em args
    total *= arg # Multiplica o total pelo argumento

  return total # Retorna o total

mult_numeros = multiplica_argumentos(*numeros) # Desempacota a tupla 'numeros' e passa os argumentos para a função 'multiplica_argumentos', armazenando o valor retornado na variável 'mult_numeros'

print(mult_numeros) # Exibe o valor da variável 'mult_numeros' no console

"""
  Crie uma função que imprima se um número é par ou ímpar.
    * Retorne se o número é par ou ímpar.
"""

numero = 10 # Cria uma variável 'numero' e atribui o valor 10 a ela

def par_ou_impar(num): # Cria uma função 'par_ou_impar' que recebe um argumento 'num'
  if num % 2 == 0: # Se o resto da divisão do número por 2 for igual a 0
    return 'Par' # Retorna 'Par'
  else:
    return 'Ímpar' # Retorna 'Ímpar'

print(par_ou_impar(numero)) # Exibe o valor retornado pela função 'par_ou_impar' no console
