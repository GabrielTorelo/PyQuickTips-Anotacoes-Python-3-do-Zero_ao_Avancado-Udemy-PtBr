# Importa o módulo os (usado para manipular o sistema operacional)
from os import getcwd, path, rename

# Captura o diretorio atual
diretorio_atual = getcwd()
print('Diretorio atual:', diretorio_atual)

# Diretorio a ser renomeado
diretorio_renomeado = path.join(diretorio_atual, 'copiado')

# Novo nome do diretorio
diretorio_novo = path.join(diretorio_atual, 'renomeado')

# Tenta renomear o diretorio
try:
  print('Renomeando diretorio...')
  
  # Renomeia o diretorio
  rename(diretorio_renomeado, diretorio_novo)

  print('\nDiretorio renomeado com sucesso!')
  print('Origem:', diretorio_renomeado)
  print('Destino:', diretorio_novo)
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao renomear diretorio:', e)
