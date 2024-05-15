"""
  Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string.
"""

nome = 'Gabriel Torelo'
tamanho_nome = len(nome) # Pega o tamanho da string

print(f'O nome "{nome}" possui "{tamanho_nome} caracteres".\n')

"""
  Imprima os caracteres da string com um '*' antes de cada caractere.
"""

i = 0

while i < tamanho_nome:
  print('*', end='') # Usando o end='' para não pular linha
  print(nome[i], end='') # Usando o end='' para não pular linha
  i += 1 # Incrementa o contador

print('*') # Imprime o último '*' para finalizar a string
