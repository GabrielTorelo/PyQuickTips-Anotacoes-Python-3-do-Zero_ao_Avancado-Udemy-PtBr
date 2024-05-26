# Criando a classe A
class A:
  atributo_a = 'valor a'

  # Método construtor
  def __init__(self, atributo: str):
    self.atributo = atributo

  # Método para imprimir 'A'
  def metodo(self):
    print('A')

# Criando a classe B
class B(A):
  atributo_b = 'valor b'

  # Método para imprimir 'B'
  def metodo(self):
    print('B')

# Criando a classe C
class C(B):
  atributo_c = 'valor c'

  # Método que retorna o método superior (super) da classe 'B'
  # Ou seja: O método da classe 'A'
  def metodo(self):
    return super(B, self).metodo() # Retorna o método superior da classe 'B'

# Instanciando objeto do tipo C
c = C('Atributo')

c.metodo()
