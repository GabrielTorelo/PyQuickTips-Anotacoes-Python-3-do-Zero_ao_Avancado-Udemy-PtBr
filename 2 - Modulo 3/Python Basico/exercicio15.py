import random

"""
  Criar um gerador de CPF
"""

num_cpf = 0

for _ in range(10):
  num_cpf += 1

  cpf = ''
  soma_prim_dig = 0
  soma_seg_dig = 0

  for _ in range(9):
    cpf += str(random.randint(0, 9))

  for i in range(9):
    soma_prim_dig += int(cpf[i]) * (10 - i)

  prim_dig = ((soma_prim_dig * 10) % 11)

  prim_dig = 0 if prim_dig > 9 else prim_dig

  cpf += str(prim_dig)

  for i in range(10):
    soma_seg_dig += int(cpf[i]) * (11 - i)

  seg_dig = ((soma_seg_dig * 10) % 11)

  seg_dig = 0 if seg_dig > 9 else seg_dig

  cpf += str(seg_dig)

  print(f'{num_cpf}º CPF: {cpf}')
