caminho_arquivo = 'aula43.txt' # Caminho do arquivo

# --------------------------------------------
# ------- Sem fechamento automático ----------
# --------------------------------------------

arquivo = open(caminho_arquivo, 'w', encoding='utf8') # Abre o arquivo em modo de escrita
arquivo.write('Olá Mundo!\n') # Escreve no arquivo e pula uma linha
arquivo.close() # Fecha o arquivo

# --------------------------------------------
# ------- Com fechamento automático ----------
# --------------------------------------------

# Abre o arquivo em modo de escrita e o fecha automaticamente
with open(caminho_arquivo, 'w', encoding='utf8') as arquivo: 
  arquivo.write('Olá Mundo!\n') # Escreve no arquivo e pula uma linha
  arquivo.write('Olá Mundo!') # Escreve no arquivo

# Abre o arquivo em modo de leitura e o fecha automaticamente
with open(caminho_arquivo, 'r', encoding='utf8') as arquivo: 
  print(arquivo.read()) # Lê o conteúdo do arquivo
