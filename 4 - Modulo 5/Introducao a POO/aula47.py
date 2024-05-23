# Criando a classe Camera
class Camera:
  # Método construtor
  def __init__(self, nome):
    self.nome = nome
    self.filmando = False

  # O método __parar_filmar() é um método privado, pois seu nome começa com dois underlines
  def __parar_filmar(self):
    print(f'{self.nome} parou de filmar!')
    self.filmando = False
    return

  # Método para filmar
  def filmar(self):
    if self.filmando:
      self.__parar_filmar()
      return

    print(f'{self.nome} está filmando!')
    self.filmando = True

  # Método para fotografar
  def fotografar(self):
    if self.filmando:
      self.__parar_filmar()

    print(f'{self.nome} fotografou!')

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.fotografar()

# --------------------------------------------

print('\n')

# --------------------------------------------

c2.filmar()
c2.fotografar()
c2.fotografar()
