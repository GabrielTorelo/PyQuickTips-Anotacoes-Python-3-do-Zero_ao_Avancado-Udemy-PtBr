# Importando o módulo abc - Necessário para manipulação de classes abstratas
from abc import ABC, abstractmethod

# Definindo a classe abstrata Pessoa que herda de ABC
class Pessoa(ABC):

  # Método construtor
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  # Método abstrato que deve ser implementado nas subclasses (classes filhas)
  @abstractmethod
  def falar_oi(self):
    pass

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

# Criando a classe Cliente que herda a classe Pessoa
class Cliente(Pessoa):

  # Implementando o método abstrato
  def falar_oi(self):
    print(f'Oi {self.get_nome}, como está?')

# Instanciando objeto do tipo Cliente
p1 = Cliente("João", 30)

p1.falar_oi()
