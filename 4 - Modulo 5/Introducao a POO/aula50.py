# Cria uma classe Computador com os métodos getter e setter para manipular a cor do computador
class Computador:

  # Método construtor
  def __init__(self, cor: str):
    self._cor = cor

  @property # Getter
  def get_cor(self):
    return self._cor # Retorna a cor do computador

  @get_cor.setter # Setter
  def set_cor(self, nova_cor: str):
    self._cor = nova_cor # Altera a cor do computador

# Criação de objetos da classe Computador
notebook = Computador('preto')
pc = Computador('cinza')

# Pegando a cor dos objetos, usando o getter
print(f'Notebook tem a cor "{notebook.get_cor}" | PC tem a cor "{pc.get_cor}"')

pc.set_cor = 'azul' # Altera a cor do PC, usando o setter

print(f'Agora o PC tem a cor: "{pc.get_cor}"')

# --------------------------------------------

print('\n')

# --------------------------------------------

# Usando o nome do setter como o nome do atributo
class Computador:

  # Método construtor
  def __init__(self, cor: str):
    self.cor = cor

  @property # Getter
  def get_cor(self):
    return self._cor # Retorna a cor do computador

  @get_cor.setter # Setter
  def cor(self, nova_cor: str):
    print('Passou pelo setter!')
    self._cor = nova_cor # Altera a cor do computador

# Criação de objetos da classe Computador (como o setter tem o mesmo nome do atributo, passa automaticamente pelo setter ao criar o objeto)
notebook = Computador('vermelho')
pc = Computador('azul')

print(f'Notebook tem a cor "{notebook.get_cor}" | PC tem a cor "{pc.get_cor}"')
