# Importa o módulo os (usado para manipular o sistema operacional)
from os import path, walk, unlink

# Captura o caminho absoluto do arquivo
caminho = path.abspath('.')

print('Caminho absoluto:', caminho)


# CUIDADO: O método unlink() exclui um arquivo!!!
caminho_excluir = 'Users\\USER\\Downloads\\arquivo.txt'
unlink(caminho_excluir) # Exclui o arquivo
# CUIDADO: O método unlink() exclui um arquivo!!!


# Percorre todo o caminho e exibe os diretórios e arquivos
for raiz, diretorios, arquivos in walk(caminho):
  base = path.basename(raiz) # Captura o nome do diretório raiz

  if base == 'venv': # Se o diretório raiz for 'venv', interrompe o loop
    break

  print('Raiz:', raiz)
  
  # Exibe os arquivos ou diretórios contidos no diretório raiz
  for diretorio in diretorios:
    if diretorio == '__pycache__': # Se o diretório for '__pycache__', pula para a próxima iteração
      continue

    print(' ', 'Diretório:', diretorio)
