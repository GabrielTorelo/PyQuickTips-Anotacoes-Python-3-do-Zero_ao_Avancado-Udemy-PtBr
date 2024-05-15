frase = 'Aprendendo Python de forma prática, rápida e objetiva'

i = 0
apareceu = 0
letra = ''

while i < len(frase):
  if frase[i] == ' ':
    i += 1
    continue

  if frase.count(frase[i]) >= apareceu:
    apareceu = frase.count(frase[i])
    letra = frase[i]

  i += 1

print(f'A letra que mais apareceu foi "{letra}" e apareceu "{apareceu} vezes"')
