class Pessoa:

  # Método construtor que é chamado quando a instância é criada
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
  
  # Método destrutor que é chamado quando a instância é deletada
  def __del__(self):
    print("A instância foi deletada")

  # Método para imprimir a representação de string oficial do objeto
  def __repr__(self):
    class_name = type(self).__name__
    return f"{class_name}(nome={self.nome!r}, idade={self.idade!r})"

  # Método para imprimir a representação de string do objeto
  def __str__(self):
    return f"Sou mostrada ao chamar a instância"

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

# Imprimindo a instância
print(p1)

# Imprindo a representação de string oficial da instância
print(repr(p1))

# Deletando a instância
del p1
