# Cria o método 'meu_repr' que retorna um __repr__ personalizado
def meu_repr(self):
  class_name = self.__class__.__name__
  class_dict = self.__dict__
  return f'{class_name}({class_dict})'

# Método decorador que adiciona o método __repr__ a uma classe
def adiciona_repr(cls: object):
  cls.__repr__ = meu_repr
  return cls

# Utilizando o decorador 'adiciona_repr'
@adiciona_repr
class Time: # Classe Time
  def __init__(self, nome):
    self.nome = nome

# Utilizando o decorador 'adiciona_repr'
@adiciona_repr
class Planeta: # Classe Planeta
  def __init__(self, nome):
    self.nome = nome

# Criando instâncias da classe Time
brasil = Time('Brasil')
portugal = Time('Portugal')

# Criando instâncias da classe Planeta
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)