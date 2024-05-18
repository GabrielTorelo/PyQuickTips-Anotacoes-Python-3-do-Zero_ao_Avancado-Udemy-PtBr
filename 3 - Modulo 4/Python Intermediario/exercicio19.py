"""
  Crie um jogo de acertar qual a letra usando conjuntos ('set()')
"""

letras = set()

print('Adivinhe qual a letra!')

while True:
  user_input = input('Digite uma letra: ')
  letras.add(user_input.lower())


  if 'g' in letras:
    print('Parabéns, você acertou a letra! A letra era "G"')
    break

  print(letras)
