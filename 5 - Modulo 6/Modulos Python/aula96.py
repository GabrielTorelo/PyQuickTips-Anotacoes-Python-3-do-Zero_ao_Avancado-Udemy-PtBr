# Importa o módulo csv (usado para manipular arquivos CSV)
from csv import reader, writer, DictReader

# Cria uma lista de listas com os dados que serão escritos no arquivo CSV
dados = [
  ['Nome', 'Idade', 'Cidade'],
  ['João', 30, 'São Paulo'],
  ['Maria', 25, 'Rio de Janeiro']
]

try:
  # Abre o arquivo CSV para escrita
  with open('aula96.csv', 'w', newline='') as arquivo:

    # Cria um objeto de escrita
    escritor = writer(arquivo)

    # Escreve os dados no arquivo
    escritor.writerows(dados)
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao criar o CSV:', e)


# --------------------------------------------

print('\n')

# --------------------------------------------

try:
  # Abre o arquivo CSV para leitura
  with open('aula96.csv', 'r') as arquivo:

    # Cria um objeto de leitura
    leitor = reader(arquivo)

    # Lê os dados do arquivo
    for linha in leitor:
      print(linha)
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao abrir o CSV:', e)

# --------------------------------------------

print('\n')

# --------------------------------------------

try:
  # Abre o arquivo CSV para leitura
  with open('aula96.csv', 'r') as arquivo:

    # Cria um objeto de leitura
    leitor = DictReader(arquivo)

    # Lê os dados do arquivo
    for linha in leitor:
      print(linha)
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao abrir o CSV:', e)
