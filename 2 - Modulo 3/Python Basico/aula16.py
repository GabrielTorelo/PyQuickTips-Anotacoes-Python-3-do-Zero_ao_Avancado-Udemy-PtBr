nomes = ['Pedro', 'João', 'Leticia']

for n in nomes:
  print(n)

# --------------------------------------------

print('\n')

# --------------------------------------------

i = 0

while i < len(nomes):
  print(nomes[i])
  i += 1

  if i == 2:
    break

# --------------------------------------------

print('\n')

# --------------------------------------------

i = 0

while i < len(nomes):
  if i == 1:
    i += 1
    continue

  print(nomes[i])
  i += 1
