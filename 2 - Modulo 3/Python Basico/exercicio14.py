"""
  Verificar se um CPF enviado pelo usuário é válido
"""

while True:
  soma_prim_dig = 0
  soma_seg_dig = 0
  prim_dig_valido = False
  seg_dig_valido = False
  cpf = input("Digite o CPF: ")
  
  if len(cpf) == 14:
    cpf = cpf.replace(".", "").replace("-", "")
  elif len(cpf) < 11 or len(cpf) > 14:
    print("Informe um CPF válido\n")
    continue
  
  if cpf[0] * len(cpf) == cpf:
    print("Informe um CPF válido\n")
    continue

  try:
    int(cpf)
  except ValueError:
    print("Informe um CPF válido\n")

  for i in range(9):
    soma_prim_dig += int(cpf[i]) * (10 - i)

  prim_dig = ((soma_prim_dig * 10) % 11)

  prim_dig = 0 if prim_dig > 9 else prim_dig

  if prim_dig == int(cpf[9]):
    prime_dig_valido = True
  else:
    print("\n1º dígito do CPF inválido")
    print(f"1º dígito deveria ser: {prim_dig}")
    print(f"1º dígito do CPF: {cpf[9]}\n")
    continue

  for i in range(10):
    soma_seg_dig += int(cpf[i]) * (11 - i)

  seg_dig = ((soma_seg_dig * 10) % 11)

  seg_dig = 0 if seg_dig > 9 else seg_dig

  if seg_dig == int(cpf[10]):
    seg_dig_valido = True
  else:
    print("\n2º dígito do CPF inválido")
    print(f"2º dígito deveria ser: {seg_dig}")
    print(f"2º dígito do CPF: {cpf[10]}\n")
    continue

  if prime_dig_valido and seg_dig_valido:
    print("\nCPF válido!\n")
    break
