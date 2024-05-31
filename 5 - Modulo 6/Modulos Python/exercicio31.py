"""
  Maria pegou um empréstimo de 1.000.000 para realizar o pagamento em 5 anos.
  A data em que ela pegou o empréstimo foi 20/12/2020 e o vencimento de cada parcela
  é no dia 20 de cada mês.
    * Crie a data do empréstimo
    * Crie a data do final do empréstimo
    * Mostre todas as datas de vencimento e o valor de cada parcela
"""

# Importa módulos para manipulação de datas
from datetime import  datetime
from dateutil.relativedelta import relativedelta

data_inicio = datetime(2020, 12, 20) # Cria a data do empréstimo
data_fim = data_inicio + relativedelta(years=5) # Cria a data do final do empréstimo
qtd_parcelas = (data_fim.year - data_inicio.year) * 12 + (data_fim.month - data_inicio.month) # Calcula a quantidade de parcelas
valor_parcela = 1000000 / qtd_parcelas # Podemos usar "1_000_000" para melhor visualização (não muda nada, ou seja, continua sendo um inteiro)

print("----------------------------------------------")
print(f"Data do empréstimo: {data_inicio.strftime('%d/%m/%Y')}")
print(f"Data do final do empréstimo: {data_fim.strftime('%d/%m/%Y')}")
print(f"Quantidade de parcelas: {qtd_parcelas} | Valor da parcela: R$ {valor_parcela:.2f}")
print("----------------------------------------------\n")

for i in range(0, qtd_parcelas):
  data_vencimento = data_inicio + relativedelta(months=i) # Calcula a data de vencimento (dia 20 de cada mês)
  print(f"Parcela {i+1}: {data_vencimento.strftime('%d/%m/%Y')} -> R$ {valor_parcela:.2f}")
