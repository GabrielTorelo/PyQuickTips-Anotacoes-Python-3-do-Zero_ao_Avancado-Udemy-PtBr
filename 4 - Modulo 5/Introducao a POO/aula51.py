# Criando uma classe Marceneiro
class Marceneiro:

  # Método construtor
  def __init__(self, nome: str):
    self.nome = nome
  
  # Método para imprimir
  def __str__(self) -> str:
    return f'{self.nome} está usando a ferramenta: {self.get_ferramenta.imprimir()}'

  @property # Getter para nome
  def get_nome(self):
    return self._nome

  @property # Getter para ferramenta
  def get_ferramenta(self):
    return self._ferramenta

  @get_nome.setter # Setter para nome
  def nome(self, nome: str):
    self._nome = nome

  @get_ferramenta.setter # Setter para ferramenta
  def ferramenta(self, ferramenta: str):
    self._ferramenta = ferramenta

# Criando uma classe Ferramenta_Madeira
class Ferramenta_Madeira:

  # Método construtor
  def __init__(self, nome: str):
    self.nome = nome

  # Método para imprimir
  def imprimir(self) -> str:
    return self.get_nome

  @property # Getter para nome
  def get_nome(self):
    return self._nome

  @get_nome.setter # Setter para nome
  def nome(self, nome: str):
    self._nome = nome

# Instanciando objetos do tipo Ferramenta_Madeira
ferram1 = Ferramenta_Madeira('Serra')
ferram2 = Ferramenta_Madeira('Formão')

# Instanciando objetos do tipo Marceneiro
m1 = Marceneiro('José')
m2 = Marceneiro('Júlio')

# Atribuindo ferramentas aos marceneiros
m1.ferramenta = ferram1
m2.ferramenta = ferram2

print(m1)
print(m2)

# Acessando ferramentas diretamente
print(f'\nFerramenta é {ferram1.imprimir()}')
print(f'Ferramenta é {ferram2.imprimir()}')

# Acessando ferrementa pelo Marceneiro
print(f'\n{m1.get_nome} está com a ferramenta: {m1.get_ferramenta.imprimir()}')
