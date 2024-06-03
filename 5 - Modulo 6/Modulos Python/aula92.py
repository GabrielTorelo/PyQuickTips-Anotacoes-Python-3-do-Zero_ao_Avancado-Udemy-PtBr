# Importa o módulo os (usado para manipular o sistema operacional)
from os import getcwd, path

# Importa o módulo shutil (usado para manipular arquivos)
from shutil import move

# Captura o diretorio atual
diretorio_atual = getcwd()
print('Diretorio atual:', diretorio_atual)

# Diretorio a ser movido
diretorio_copiado = path.join(diretorio_atual, 'diretorio_copiado')

# Diretorio de destino
diretorio_novo = path.join(diretorio_atual, 'copiado')

# Tenta mover o diretorio
try:
  print('Movendo diretorio...')
  
  # Move o diretorio
  move(diretorio_copiado, diretorio_novo)

  print('\nDiretorio movido com sucesso!')
  print('Origem:', diretorio_copiado)
  print('Destino:', diretorio_novo)
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao mover diretorio:', e)
