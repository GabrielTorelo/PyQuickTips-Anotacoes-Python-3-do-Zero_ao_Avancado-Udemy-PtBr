# Importando a classe NamedTuple do módulo typing
from collections import namedtuple
from typing import NamedTuple

# Criando a classe Funcionario com os atributos name e id
class Funcionario(NamedTuple):
  name: str = 'Sem Nome' # Atributo name do tipo string
  id: int = 0 # Atributo id do tipo inteiro

# Criando uma tupla nomeada chamada Carta com os atributos valor e naipe
Carta = namedtuple(
  'Carta', ['valor', 'naipe'],
  defaults=['VALOR', 'NAIPE']
)

# Criando uma instância da classe Funcionario
func1 = Funcionario('José', 1234)

# Criando uma instância da classe Carta
carta1 = Carta('A', '❤️')

print(func1)
print(carta1)
