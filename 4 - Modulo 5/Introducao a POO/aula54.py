# Criando a classe Animal
class Animal:

  # Método construtor
  def __init__(self, nome: str):
    print('Estou no método construtor da classe "Animal"')
    self.nome = nome

  # Método comer
  def comer(self):
    print(f"{self.get_nome} está comendo")

  @property # Getter
  def get_nome(self):
    return self._nome

  @get_nome.setter # Setter
  def nome(self, nome):
    self._nome = nome

# Criando a classe Cachorro que herda a classe Animal
class Cachorro(Animal):

  # Sobrepondo o método construtor da classe 'Animal' e chamando ele usando o 'super'
  def __init__(self, nome: str):
    print('Estou no método construtor da classe "Cachorro"')
    super().__init__(nome)

  # Método para imprimir
  def __str__(self) -> str:
    return f'{self.get_nome} é um cachorro'

  # Método latir
  def latir(self):
    print(f"{self.get_nome} está latindo")

# Instanciando objeto do tipo Cachorro
cachorro = Cachorro("Rex")

print(cachorro)

cachorro.latir()
cachorro.comer()
