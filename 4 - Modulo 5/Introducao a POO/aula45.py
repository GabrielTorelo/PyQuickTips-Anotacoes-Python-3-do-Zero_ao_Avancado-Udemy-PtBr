class Pessoa:
  def cumprimentar(self):
    return f"Olá, seja muito bem-vindo"

p1 = Pessoa()
p1.nome = "João"
p1.idade = 30

print(p1.nome)
print(p1.idade)
print(p1.cumprimentar())

# --------------------------------------------

print('\n')

# --------------------------------------------

class Humano:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def cumprimentar(self):
    print(f"Olá, seja muito bem-vindo {self.nome}")

h1 = Humano("João", 30)

print(f"{h1.nome} tem {h1.idade} anos")
