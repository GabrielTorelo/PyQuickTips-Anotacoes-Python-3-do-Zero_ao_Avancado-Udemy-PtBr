x = 1

def escopo():
  x = 10

  def dentro():
    y = 2
    print(x, y)

  dentro()

  print(x)

escopo()

# --------------------------------------------

print('\n')

# --------------------------------------------


z = 1

def minha_funcao():
  z = 10
  return z

print(minha_funcao())
print(z)
