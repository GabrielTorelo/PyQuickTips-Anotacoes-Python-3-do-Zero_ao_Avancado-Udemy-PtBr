# Importando o módulo abc - Necessário para manipulação de classes abstratas
from abc import ABC, abstractmethod

# Criando a classe Animal
class Animal(ABC):

  # Método construtor
  def __init__(self, nome):
    self.nome = nome
  
  # Método abstrato (deve ser implementado nas classes filhas)
  @abstractmethod
  def emitir_som(self) -> bool:
    pass

  @property # Getter
  def get_nome(self):
    return self._nome

  @get_nome.setter # Setter
  def nome(self, nome):
    self._nome = nome

# Criando a classe Cachorro que herda a classe Animal
class Cachorro(Animal):
  
  # Método emitir_som sobrescrito
  def emitir_som(self) -> bool:
    print(f'{self.get_nome} está latindo')
    return True

# Criando a classe Gato que herda a classe Animal
class Gato(Animal):

  # Método emitir_som sobrescrito
  def emitir_som(self) -> bool:
    print(f'{self.get_nome} está miando')
    return True

# Instanciando objeto do tipo Cachorro
cachorro = Cachorro('Rex')

# Instanciando objeto do tipo Gato
gato = Gato('Mingau')

cachorro.emitir_som()
gato.emitir_som()

# --------------------------------------------

print('\n')

# --------------------------------------------

# Função sons que recebe um objeto do tipo Animal
def sons(animal: Animal):

  # Verifica se o som foi emitido
  som_emitido = animal.emitir_som() # Chama o método emitir_som (da classe filha)

  # Verifica se o som foi emitido
  if som_emitido:
    print('O som foi emitido!\n')
  else:
    print('O som NÃO foi emitido!\n')

# Chamando a função sons passando um objeto que herda a classe Animal
sons(gato)
sons(cachorro)
