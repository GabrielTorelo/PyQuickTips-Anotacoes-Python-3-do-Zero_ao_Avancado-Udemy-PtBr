"""
  Calculo do segundo dígito do CPF

  * Colete a soma dos 9 primeiros dígitos do CPF,
    MAIS O PRIMEIRO DIGITO, multiplicando cada um
    dos valores por uma contagem regressiva
    começando de 11
  * Somar todos os resultados
  * Multiplicar o resultado anterior por 10
  * Obter o resto da divisão da conta anterior por 11

  Se o resultado anterior for maior que 9:
    resultado é 0
  Se o resultado anterior for menor que 9:
    resultado é ele mesmo
"""

cpf = "746.824.890-70" # CPF Válido
# cpf = "746.824.890-71" # CPF Inválido

cpf = cpf.replace(".", "").replace("-", "")

soma_seg_dig = 0

for i in range(10):
	soma_seg_dig += int(cpf[i]) * (11 - i)

seg_dig = ((soma_seg_dig * 10) % 11)

seg_dig = 0 if seg_dig > 9 else seg_dig

if seg_dig == int(cpf[10]):
	print("2º dígito do CPF válido")
else:
	print("\n2º dígito do CPF inválido")
	print(f"2º dígito deveria ser: {seg_dig}")
	print(f"2º dígito do CPF: {cpf[10]}")
