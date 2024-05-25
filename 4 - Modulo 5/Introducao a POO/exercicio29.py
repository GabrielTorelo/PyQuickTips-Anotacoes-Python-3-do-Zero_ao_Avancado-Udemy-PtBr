"""
  1 - Crie uma classe Carro
    (Atributos: nome, preco)
  1.1 - Crie uma classe Motor
    (Atributos: nome, valvulas)
  1.2 - Crie uma classe Fabricante
    (Atributos: nome, sigla)

  2.1 - Faça a ligação entre Carro e Motor
    ("Carro" tem um "Motor" | "Motor" pode ser de vários "Carros")
  2.2 - Faça a ligação entre Carro e um Fabricante
    ("Carro" tem um "Fabricante" | "Fabricante" pode fabricar vários "Carros")
  
  3 - Imprima o nome do carro, motor e fabricante no console
"""

# Criando a classe Motor
class Motor:

  # Método construtor
  def __init__(self, nome: str, valvulas: int):
    self.nome = nome
    self.valvulas = valvulas

  # Método para imprimir
  def __str__(self) -> str:
    return f'{self.get_nome} - {self.get_valvulas} valvulas'

  @property # Getter
  def get_nome(self):
    return self._nome
  
  @property # Getter
  def get_valvulas(self):
    return self._valvulas

  @get_nome.setter # Setter
  def nome(self, nome: str):
    self._nome = nome
  
  @get_valvulas.setter # Setter
  def valvulas(self, valvulas: int):
    self._valvulas = valvulas

# Criando a classe Fabricante
class Fabricante:

  # Método construtor
  def __init__(self, nome: str, sigla: str):
    self.nome = nome
    self.sigla = sigla

  # Método para imprimir
  def __str__(self) -> str:
    return f'{self.get_sigla}-{self.get_nome}'

  @property # Getter
  def get_nome(self):
    return self._nome
  
  @property # Getter
  def get_sigla(self):
    return self._sigla
  
  @get_nome.setter # Setter
  def nome(self, nome: str):
    self._nome = nome

  @get_sigla.setter # Setter
  def sigla(self, sigla: str):
    self._sigla = sigla

# Criando a classe Carro
class Carro:

  # Método construtor
  def __init__(self, nome: str, preco: float, motor: Motor, fabricante: Fabricante):
    self.nome = nome
    self.preco = preco
    self.motor = motor
    self.fabricante = fabricante

  # Método para imprimir
  def __str__(self) -> str:
    return f'O carro "{self.get_nome}" tem o '\
      f'motor "{self.get_motor}", é '\
      f'fabricado pelo(a) "{self.get_fabricante}" e '\
      f'custa R$ {self.get_preco:.2f}'

  @property # Getter
  def get_nome(self):
    return self._nome

  @property # Getter
  def get_preco(self):
    return self._preco

  @property # Getter
  def get_motor(self):
    return self._motor

  @property # Getter
  def get_fabricante(self):
    return self._fabricante

  @get_nome.setter # Setter
  def nome(self, nome: str):
    self._nome = nome

  @get_preco.setter # Setter
  def preco(self, preco: float):
    self._preco = preco

  @get_motor.setter # Setter
  def motor(self, motor: Motor):
    self._motor = motor

  @get_fabricante.setter # Setter
  def fabricante(self, fabricante: Fabricante):
    self._fabricante = fabricante

# Instanciando objetos do tipo Motor e Fabricante
motor1 = Motor('1.0 L 3-cylinder', 8)
fab1 = Fabricante('Chevrolet', 'GM')

# Instanciando objetos do tipo Carro
car1 = Carro('Onix', 75000.00, motor1, fab1)
car2 = Carro('Tracker', 119900.00, motor1, fab1)

print(car1)
print(car2)
