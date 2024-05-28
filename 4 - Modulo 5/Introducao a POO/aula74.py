# Criando a classe Multiplicar
class Multiplicar:

  # Método construtor
  def __init__(self, mult: int):
    self.mult = mult

  # Método que permite chamar a instância da classe como uma função
  def __call__(self, func: callable):
    def wrapper(*args, **kwargs): # Função interna
      result = func(*args, **kwargs)
      return round(result * self.mult, 2)
    return wrapper # Retorna a função interna
  
  @property # Getter
  def get_mult(self):
    return self._mult
  
  @get_mult.setter # Setter
  def mult(self, mult: int):
    self._mult = mult

def soma_e_multiplica(x: float, y: float, mult: int) -> float:

  # Decorando a função 'soma' com a classe Multiplicar, passando o valor recebido no parâmetro 'mult'
  @Multiplicar(mult)
  def soma():
    return x + y
  return soma()

# Outra forma de decorar uma função com a classe Multiplicar
@Multiplicar(2)
def soma(a: float, b: float):
  return a + b

print(f'Soma: {soma(2, 3)}')

print(f'Soma e Multiplica: {soma_e_multiplica(x=2.7, y=3.97, mult=6)}')