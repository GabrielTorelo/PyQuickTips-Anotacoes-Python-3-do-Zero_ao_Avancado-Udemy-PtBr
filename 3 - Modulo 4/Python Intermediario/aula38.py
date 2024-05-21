# Funções decoradora (recebe uma função e retorna ela mesma passando valores)
def retornaNum(func):
  print('Entrou na função decoradora! Função: ', func)
  return func(1, 2) # Chama e retorna a função decorada, passando 2 valores

@retornaNum # Sugarsyntax - Açúcar sintático
# Função decorada (será chamada pela função decoradora e espera receber 2 valores)
def soma1(a, b):
  return a + b # Soma 2 valores recebidos

print('Fez a soma automaticamente (sem passar valores): ', soma1) # Retorna a função decorada

# --------------------------------------------

print('\n')

# --------------------------------------------

# Funções decoradora (recebe uma função e retorna ela mesma)
def meu_decorador(func):
  print('Entrou na função decoradora! Função: ', func)
  def embrulho():
    print('Olá, sou um decorador!')
    return func() # Chama e retorna a função decorada
  return embrulho # Retorna a função emcapsulada

@meu_decorador # Sugarsyntax - Açúcar sintático
def minha_funcao():
  print(f'Onde estou? {minha_funcao.__name__}') # Retorna em qual função está

minha_funcao()

# --------------------------------------------

print('\n')

# --------------------------------------------

# Funções decoradora (recebe uma função e retorna ela mesma)
def decora_log(func):
  def embrulho(*args):
    print(f'Você está chamando a função "{func.__name__}" com os argumentos "{args}"!')
    return func(*args) # Chama e retorna a função decorada, passando os argumentos
  return embrulho # Retorna a função emcapsulada

@decora_log # Sugarsyntax - Açúcar sintático
def soma2(a, b):
  return a + b # Soma 2 valores recebidos

soma2(1, 2)
