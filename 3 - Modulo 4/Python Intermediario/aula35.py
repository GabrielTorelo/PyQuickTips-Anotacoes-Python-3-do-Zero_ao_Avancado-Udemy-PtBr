try:
  a = 10 / 0 # Tentando dividir um número por zero
  print(a)
except ZeroDivisionError: # Erro lançado quando ocorre uma divisão por zero
  print("Erro: divisão por zero")

try:
  file = open("arquivo.txt", "r") # Tentando abrir um arquivo que não existe
except FileNotFoundError: # Erro lançado quando o arquivo não é encontrado
  print("Erro: arquivo não encontrado")

try:
  a = int(input("Digite um número: ")) # Tentando converter um valor digitado para inteiro
  print(a)
except ValueError: # Erro lançado quando o valor digitado não é um número
  print("Erro: valor inválido")

try:
  a = [1, 2, 3]
  print(a[3]) # Tentando acessar um índice que não existe
except Exception: # Erro genérico
  print("Erro desconhecido!")

# --------------------------------------------

print('\n')

# --------------------------------------------

try:
  file = open("arquivo.txt", "r") # Tentando abrir um arquivo que não existe
except FileNotFoundError as error: # Erro lançado quando o arquivo não é encontrado, capturando a mensagem de erro
  print("Erro: arquivo não encontrado -", error)

# --------------------------------------------

print('\n')

# --------------------------------------------

n1 = 10
n2 = -2

n1 / n2 # Erro: divisão por zero
raise ValueError("O valor não pode ser negativo") # Lançando um erro manualmente
