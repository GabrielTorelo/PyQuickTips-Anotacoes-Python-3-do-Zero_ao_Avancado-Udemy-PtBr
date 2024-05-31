# Importa o módulo os (usado para manipular o sistema operacional)
from os import path, listdir

# Captura o caminho absoluto do arquivo
caminho = path.abspath('.')

print('Caminho absoluto:', caminho)

# Lista os arquivos e diretórios do caminho absoluto
for diretorio in listdir(caminho):
  # Captura o caminho completo do diretório
  caminho_completo = path.join(caminho, diretorio)

  # Verifica se o caminho completo é um diretório
  if not path.isdir(caminho_completo):
    continue

  # Lista os arquivos e diretórios do caminho completo
  for arquivos in listdir(caminho_completo):
    print(arquivos)
