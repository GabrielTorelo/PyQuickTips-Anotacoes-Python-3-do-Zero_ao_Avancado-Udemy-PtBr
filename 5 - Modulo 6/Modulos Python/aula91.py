# Importa o módulo os (usado para manipular o sistema operacional)
from os import getcwd, path

# Importa o módulo shutil (usado para manipular arquivos)
from shutil import copytree, rmtree

# Captura o diretorio home
HOME = path.expanduser('~')
print('HOME:', HOME)

# Captura o diretorio desktop
DESKTOP = path.join(HOME, 'Desktop')
print('DESKTOP:', DESKTOP)

# Diretorio a ser copiado
DIRETORIO_COPIAR = path.join(DESKTOP, 'diretorio_copiar')
print('DIRETORIO_COPIAR:', DIRETORIO_COPIAR)

# Captura o diretorio atual
diretorio_atual = getcwd()
print('Diretorio atual:', diretorio_atual)

# Diretorio de destino
diretorio_novo = path.join(diretorio_atual, 'diretorio_copiado')

# Tenta copiar o diretorio
try:
  print('Copiando diretorio...')

  # Copia o diretorio para o diretorio atual (caso exista, sobrescreve)
  copytree(DIRETORIO_COPIAR, diretorio_novo, dirs_exist_ok=True)

  print('\nDiretorio copiado com sucesso!')
  print('Origem:', DIRETORIO_COPIAR)
  print('Destino:', diretorio_atual)
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao copiar diretorio:', e)

# Loop para receber a resposta do usuário
while True:

  # Pergunta ao usuário se deseja apagar o diretorio antigo
  user_input = input('\n\nDeseja apagar o diretorio antigo? [S]im ou [N]ão?')

  if user_input.lower() == 's': # Se a resposta for sim
    try:
      print('Apagando diretorio antigo...')
      rmtree(DIRETORIO_COPIAR)
      print('Diretorio antigo apagado com sucesso!')
    except Exception as e: # Trata caso ocorra algum erro
      print('Erro ao apagar diretorio:', e)
    break
  elif user_input.lower() == 'n': # Se a resposta for não
    print('Diretorio antigo não foi apagado!')
    break
  else: # Se a resposta for inválida
    print('Opção inválida!')
