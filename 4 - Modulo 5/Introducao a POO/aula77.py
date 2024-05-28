# Importando a classe 'Enum' e a função 'auto' do módulo "enum"
from enum import Enum, auto

# Criando uma classe DiaDaSemana que herda de Enum
class DiaDaSemana(Enum):

  # Definindo os valores da classe (o 'auto' cria um valor automático para cada atributo)
  SEGUNDA = auto()
  TERCA = auto()
  QUARTA = auto()
  QUINTA = auto()
  SEXTA = auto()
  SABADO = auto()
  DOMINGO = auto()

# Percorrendo os valores da classe DiaDaSemana
for dia in DiaDaSemana:
  print(dia.name) # Imprimindo o nome de cada atributo
