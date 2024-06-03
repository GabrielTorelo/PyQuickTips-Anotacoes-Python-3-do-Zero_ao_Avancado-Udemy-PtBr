# Importa o módulo os (usado para manipular o sistema operacional)
from os import walk, getcwd, path

# Importa o módulo shutil (usado para manipular arquivos)
from shutil import copy

# Captura o diretorio home
HOME = path.expanduser('~')
print('HOME:', HOME)

# Captura o diretorio desktop
DESKTOP = path.join(HOME, 'Desktop')
print('DESKTOP:', DESKTOP)

# Captura o diretorio atual
diretorio_atual = getcwd()
print('Diretorio atual:', diretorio_atual)

# Nome do arquivo a ser copiado
arquivo_copiar = 'arquivo_copiar.txt'

# Percorre o diretorio desktop
for raiz, diretorios, arquivos in walk(DESKTOP):

  # Percorre os arquivos
  for arquivo in arquivos:

    # Verifica se o arquivo foi encontrado
    if arquivo == arquivo_copiar:
      print('\nArquivo encontrado:', arquivo)
      origem = path.join(raiz, arquivo) # Caminho do arquivo a ser copiado

      try: # Tenta copiar o arquivo
        print('Copiando arquivo...')

        # Copia o arquivo para o diretorio atual
        copy(origem, diretorio_atual)

        print('\nArquivo copiado com sucesso!')
        print('Origem:', raiz)
        print('Destino:', diretorio_atual)
      except Exception as e: # Trata caso ocorra algum erro
        print('Erro ao copiar arquivo:', e)
        break
