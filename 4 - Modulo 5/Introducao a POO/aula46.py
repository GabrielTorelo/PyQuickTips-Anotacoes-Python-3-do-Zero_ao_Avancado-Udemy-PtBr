class Carro:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  def descricao(self):
    return f"O veículo é um {self.marca} {self.modelo} do ano {self.ano}"
  
car1 = Carro("Chevrolet", "Onix", 2020)
print(car1.descricao())
