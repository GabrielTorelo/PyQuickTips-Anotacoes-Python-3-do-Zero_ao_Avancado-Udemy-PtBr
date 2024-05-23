# Criando a classe Pessoa
class Pessoa:
  numero_de_pessoas = 0  # Atributo de classe

  # Método construtor
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    Pessoa.numero_de_pessoas += 1 # Incrementando 1 a cada instância da classe criada

  @classmethod # Método de classe
  def criar_com_idade_30(cls, nome):
    return cls(nome, 30)

  @classmethod # Método de classe
  def exibir_numero_de_pessoas(cls):
    print(f"Número de pessoas criadas: {cls.numero_de_pessoas}")

# Criando instâncias da classe Pessoa
p1 = Pessoa("Alice", 25)
p2 = Pessoa.criar_com_idade_30("Bob")

print(f"{p1.nome} tem {p1.idade} anos") # Exibindo os atributos da 1ª pessoa
print(f"{p2.nome} tem {p2.idade} anos\n") # Exibindo os atributos da 2ª pessoa


# Exibindo o número de pessoas criadas
Pessoa.exibir_numero_de_pessoas()
