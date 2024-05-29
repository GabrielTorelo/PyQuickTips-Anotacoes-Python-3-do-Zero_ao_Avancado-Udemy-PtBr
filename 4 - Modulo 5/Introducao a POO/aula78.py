# Importando a classe dataclass do módulo dataclasses (usado para criar classes com menos código)
from dataclasses import dataclass

# Criando a classe Pessoa com os atributos nome e idade
@dataclass # Decorator que transforma a classe em uma dataclass
class Pessoa:
  nome: str # Atributo nome do tipo string
  idade: int # Atributo idade do tipo inteiro

# Criando a classe Ponto com os atributos x e y
@dataclass(frozen=True) # Passando o parâmetro frozen=True no decorator para tornar a classe imutável
class PontoImutavel:
  x: int # Atributo x do tipo inteiro
  y: int # Atributo y do tipo inteiro

@dataclass(order=True) # Passando o parâmetro order=True no decorator para tornar a classe ordenável
class PontoOrdenado:
  x: int # Atributo x do tipo inteiro
  y: int # Atributo y do tipo inteiro

@dataclass(eq=False) # Passando o parâmetro eq=False no decorator para não gerar o método '__eq__'
class PontoSemIgual:
  x: int # Atributo x do tipo inteiro
  y: int # Atributo y do tipo inteiro

# Criando uma instância da classe Pessoa
p1 = Pessoa('Luiz', 26)

# Criando uma instância da classe PontoImutavel
p2 = PontoImutavel(10, 20)

# Criando lista de instâncias da classe PontoOrdenado
lista = [PontoOrdenado(10, 23), PontoOrdenado(5, 25), PontoOrdenado(10, 20)]

# Criando instâncias da classe PontoSemIgual
p4 = PontoSemIgual(10, 20)
p5 = PontoSemIgual(10, 20)

# Imprimindo as instâncias
print(p1) # Saída: Pessoa(nome='Luiz', idade=26)
p2.x = 20 # Saída: Erro - FrozenInstanceError: cannot assign to field 'x'
print(sorted(lista)) # Saída: [PontoOrdenado(x=5, y=25), PontoOrdenado(x=10, y=20), PontoOrdenado(x=10, y=23)]
print(p4 == p5) # Saída: False
