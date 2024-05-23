from math import pi

# Criando uma classe Carro com um método de classe
class Carro:

  # Método construtor
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
  
  # Método para representar a classe (retorna uma string ao chamar a classe)
  def __str__(self):
    return f"O veículo é um {self.marca} {self.modelo} do ano {self.ano}"

  @classmethod # Método de classe
  def fabrica_corolla(cls, ano):
    return cls("Toyota", "Corolla", ano)

# Criação de objetos da classe Carro
car1 = Carro("Chevrolet", "Onix", 2020)
car2 = Carro.fabrica_corolla(2023)

print(car1)
print(car2)

# --------------------------------------------

print('\n')

# --------------------------------------------

# Criando uma classe Pizza com métodos estáticos e de classe
class Pizza(object):

  # Método construtor
  def __init__(self, raio, altura):
    self.raio = raio
    self.altura = altura

  @staticmethod # Método estático
  def __calcular_area(raio):
    return pi * (raio ** 2)

  @classmethod # Método de classe
  def __calcular_volume(cls, altura, raio):
    return altura * cls.__calcular_area(raio)

  # Método para retornar o volume da pizza
  def pegar_volume(self):
    return round(self.__calcular_volume(self.altura, self.raio), 2)

# Crianção de um objeto da classe Pizza
pizza = Pizza(30, 5)

print(f'Volume da pizza: {pizza.pegar_volume()} cm³')
