"""
  Cálculo do primeiro dígito do CPF

  * Colete a soma dos 9 primeiros dígitos do CPF
    multiplicando cada um dos valores por uma
    contagem regressiva começando de 10
  * Somar todos os resultados
  * Multiplicar o resultado anterior por 10
  * Obter o resto da divisão da conta anterior por 11

  Se o resultado anterior for maior que 9:
    resultado é 0
  Se o resultado anterior for menor que 9:
    resultado é ele mesmo
"""

cpf = "746.824.890-70" # CPF Válido
# cpf = "746.824.890-80" # CPF Inválido

cpf = cpf.replace(".", "").replace("-", "")
soma_prim_dig = 0

for i in range(9):
  soma_prim_dig += int(cpf[i]) * (10 - i)

prim_dig = ((soma_prim_dig * 10) % 11)

prim_dig = 0 if prim_dig > 9 else prim_dig

if prim_dig == int(cpf[9]):
  print("1º dígito do CPF válido!")
else:
  print("\n1º dígito do CPF inválido")
  print(f"1º dígito deveria ser: {prim_dig}")
  print(f"1º dígito do CPF: {cpf[9]}")
