"""
  Converter as funções abaixo para 'lambda':

    def soma(x, y):
      return x + y

    def cria_multiplicador(multiplicador):
      def multiplica(numero):
        return numero * multiplicador
      return multiplica
"""

def executa(funcao, *args):
  return funcao(*args)

print(
  executa(
    lambda x, y:
      x + y, 
    20, 50
  )
)

cria_multiplicador = (
  executa(
    lambda multiplicador:
      lambda numero:
        numero * multiplicador,
      50
  )
)

print(cria_multiplicador(25))
