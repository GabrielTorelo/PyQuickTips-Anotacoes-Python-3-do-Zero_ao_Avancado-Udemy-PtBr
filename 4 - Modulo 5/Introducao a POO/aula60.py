# Criando a classe Pessoa
class Pessoa:

  # Método que é chamado antes do método construtor
  def __new__(cls, *args, **kwargs):
    print("Estou rodando antes do método construtor")
    return super().__new__(cls) # Chamando o método 'new' da superclasse (object)

  # Método construtor
  def __init__(self, nome, idade):
    print("Estou rodando no método construtor")
    self.nome = nome
    self.idade = idade
  
  @property # Getter
  def get_nome(self):
    return self._nome
  
  @property # Getter
  def get_idade(self):
    return self._idade
  
  @get_nome.setter # Setter
  def nome(self, nome):
    self._nome = nome
  
  @get_idade.setter # Setter
  def idade(self, idade):
    self._idade = idade

# Criando uma instância da classe Pessoa
p1 = Pessoa("Luiz", 29)

p1
