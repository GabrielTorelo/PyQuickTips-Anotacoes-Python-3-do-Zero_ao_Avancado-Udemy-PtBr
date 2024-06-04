# Importa o módulo csv (usado para manipular arquivos CSV)
from csv import DictReader, DictWriter

# Cria uma lista de dicionários com os dados que serão escritos no arquivo CSV
list_dicionario = [
  {
    'Nome': 'Paulo',
    'Idade': 27,
    'Cidade': 'São Caetano do Sul'
  },
  {
    'Nome': 'Jorge',
    'Idade': 33,
    'Cidade': 'São Bernardo do Campo'
  }
]

try:
  # Abre o arquivo CSV para escrita
  with open('aula97.csv', 'w', newline='') as arquivo:

    # Captura as colunas do dicionário
    colunas = list_dicionario[0].keys()

    # Cria um objeto de escrita
    escritor = DictWriter(arquivo, fieldnames=colunas)

    # Cria o cabeçalho do arquivo, contendo os nomes das colunas
    escritor.writeheader()

    # Escreve os dados no arquivo
    escritor.writerows(list_dicionario)
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao criar o CSV:', e)

# --------------------------------------------

print('\n')

# --------------------------------------------

try:
  # Abre o arquivo CSV para leitura
  with open('aula97.csv', 'r') as arquivo:

    # Cria um objeto de leitura
    leitor = DictReader(arquivo)

    # Lê os dados do arquivo
    for linha in leitor:
      print(linha)
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao abrir o CSV:', e)
