# Criação de fabrica de decoradores
def fabrica_decoradores(tipo: int):
  def chama_func(func):
    def embrulho(*args):
      # Caso o tipo seja 1, cria um log 
      if tipo == 1:
        print(f'Você está chamando a função "{func.__name__}" com os argumentos "{args}"!')
      
      # Caso o contrário, exibe uma mensagem de erro
      else:
        print('Tipo de decorador não encontrado!')
      return func(*args) # Chama e retorna a função decorada, passando os argumentos
    return embrulho # Retorna a função emcapsulada
  
  return chama_func

@fabrica_decoradores(1) # Decorador com parâmetro
def soma2(a, b):
  return a + b # Soma 2 valores recebidos

print('Resultado da soma: ', soma2(1, 5))
