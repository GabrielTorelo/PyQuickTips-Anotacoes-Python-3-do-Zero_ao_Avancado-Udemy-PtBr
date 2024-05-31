"""
  Repita o exercício 31, mas agora, peça para o usuário informar o
  valor do empréstimo e a quantidade de anos:
    * Acrescente um juros de 12% ao ano
    * Crie a data do empréstimo (data_atual)
    * Crie a data do final do empréstimo (data_atual + qtd_anos)
    * Criar a quantidade de parcelas (qtd_anos * 12)
    * Mostre todas as datas de vencimento e o valor de cada parcela
"""

# Importa módulos para manipulação de datas
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Cria a data atual
data_atual = datetime.now()

# Cria loop para pegar valores válidos
while True:
  try:
    # Pede para o usuário informar o valor do empréstimo e a quantidade de anos
    valor_emprestado = float(input("Digite o valor do empréstimo: "))
    qtd_anos = int(input("Digite a quantidade de anos: "))
    break
  except ValueError:
    # Caso o usuário digite um valor inválido, exibe uma mensagem de erro
    print("Digite um valor válido!\n")

juros_aa = 0.12 # Juros ao ano
qtd_parcelas = qtd_anos * 12 # Quantidade de parcelas
juros_total = (juros_aa * qtd_anos) * valor_emprestado # Juros total
data_fim = data_atual + relativedelta(years=qtd_anos) # Data do final do empréstimo
valor_emprestimo = valor_emprestado + juros_total # Valor total do empréstimo
valor_parcela = valor_emprestimo / qtd_parcelas # Valor da parcela

print("\n--------------------------------------------------------------")
print(f"Data do empréstimo: {data_atual.strftime('%d/%m/%Y')}")
print(f"Data do final do empréstimo: {data_fim.strftime('%d/%m/%Y')}")
print(f"Quantidade de parcelas: {qtd_parcelas} | Valor da parcela: R$ {valor_parcela:.2f}")
print("--------------------------------------------------------------\n")

for i in range(0, qtd_parcelas):
  data_vencimento = data_atual + relativedelta(months=i) # Calcula a data de vencimento (relativa ao dia atual)
  print(f"Parcela {i+1}: {data_vencimento.strftime('%d/%m/%Y')} -> R$ {valor_parcela:.2f}")
