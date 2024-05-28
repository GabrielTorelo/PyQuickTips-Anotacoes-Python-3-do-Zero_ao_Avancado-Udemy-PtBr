# Importando a classe 'Enum' e a função 'auto' do módulo "enum"
from enum import Enum, auto

# Criando uma classe Direcoes que herda de Enum
class Direcoes(Enum):

  # Definindo os valores da classe (o 'auto' cria um valor automático para cada atributo)
  DIREITA = auto()
  ESQUERDA = auto()
  CIMA = auto()
  BAIXO = auto()

# Função que recebe um objeto da classe Direcoes e retorna uma string
def mover(direcao: Direcoes) -> str:

  # Verificando se o argumento passado é uma instância da classe Direcoes
  if not isinstance(direcao, Direcoes):

    # Lançando uma exceção caso não seja
    raise ValueError('Direção inválida!')
  
  return f'Movendo para {direcao.name}' # Retornando a string com o nome do atributo passado

# Testando a função mover
print(mover(Direcoes.DIREITA))
print(mover(Direcoes.CIMA))
print(mover(Direcoes.BAIXO))
print(mover(Direcoes.ESQUERDA))
