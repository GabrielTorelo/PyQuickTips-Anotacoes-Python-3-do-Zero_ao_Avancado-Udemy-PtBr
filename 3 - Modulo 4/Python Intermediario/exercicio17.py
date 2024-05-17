"""
  Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
"""

def multiplicador(fator):
  def multiplica(numero):
    return numero * fator
  return multiplica

duplica = multiplicador(2)
triplica = multiplicador(3)
quadruplica = multiplicador(4)

print(f'Duplica 5: {duplica(5)}')
print(f'Triplica 5: {triplica(5)}')
print(f'Quadruplica 5: {quadruplica(5)}')
