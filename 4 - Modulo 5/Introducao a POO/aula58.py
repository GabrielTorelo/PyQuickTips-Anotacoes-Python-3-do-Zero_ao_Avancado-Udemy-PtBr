# Criando uma exceção customizada
class MyError(Exception): # Herda da classe Exception (classe base para todas as exceções)
  pass # Passa, pois a exceção customizada não possui nenhum comportamento adicional

# Função que lança a exceção customizada
def getError():

  # Lança a exceção customizada
  raise MyError('ID: 123', 'Nome do erro customizado', 'Motivo do erro customizado')

# Tratando a exceção customizada
try:
  getError() # Chama a função que lança a exceção customizada
except MyError as error:
  print(error.__class__.__name__) # Nome da classe da exceção customizada
  print(error.args) # Argumentos da exceção customizada
