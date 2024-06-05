# Importa o módulo zipfile (usado para manipular arquivos zip)
from zipfile import ZipFile

# Importa o módulo pathlib (usado para manipular caminhos de arquivos e diretórios)
from pathlib import Path

# Importa o módulo shutil (usado para manipular arquivos e diretórios)
from shutil import rmtree

# Cria uma função para criar arquivos
def criar_arquivos(qtd: int, diretorio: Path):

  # Percorre a quantidade de arquivos a serem criados
  for i in range(qtd):
    texto = f'texto_arquivo_{i+1}' # Texto que será escrito no arquivo

    try:
      # Abre o arquivo em modo escrita
      with open(diretorio / f'arquivo_{i+1}.txt', 'w') as arquivo:

        # Escreve o texto no arquivo
        arquivo.write(texto) 
    except Exception as e: # Trata caso ocorra algum erro
      print('Erro ao criar o arquivo:', e)

# Captura o caminho absoluto do arquivo
caminho = Path().absolute()

print('Caminho absoluto:', caminho)

# Cria o caminho dos arquivos que serão zipados
caminho_dir_zipar = caminho / 'arquivos_para_zipar'

print('\nCaminho do diretório para zipar:', caminho_dir_zipar)

# Verifica se o diretório existe, caso contrário, cria o diretório
caminho_dir_zipar.mkdir(exist_ok=True)

# Cria 5 arquivos no diretório 'arquivos_para_zipar'
criar_arquivos(5, caminho_dir_zipar)

# Cria o caminho do arquivo zip
caminho_zip = caminho / 'aula103.zip'

print('Caminho do arquivo zip:', caminho_zip)

# Cria um arquivo zip
with ZipFile(caminho_zip, 'w') as arquivo_zip:

  # Percorre todos os arquivos do diretório e adiciona ao arquivo zip
  for arquivo in caminho_dir_zipar.iterdir():

    # Adiciona o arquivo ao arquivo zip
    arquivo_zip.write(arquivo, arquivo.name)

# Exclui o diretório 'arquivos_para_zipar' e todos os arquivos contidos nele recursivamente
rmtree(caminho_dir_zipar)

# Abre o arquivo zip em modo leitura
with ZipFile(caminho_zip, 'r') as arquivo_zip:

  # Lista todos os arquivos do arquivo zip
  print('Arquivos zipados:', arquivo_zip.namelist())

# Cria o caminho do diretório para extrair os arquivos
caminho_dir_extrair = caminho / 'arquivos_extraidos'

print('\nCaminho do diretório para extrair:', caminho_dir_extrair)

# Abre o arquivo zip em modo leitura
with ZipFile(caminho_zip, 'r') as arquivo_zip:

  # Extrai todos os arquivos para o diretório 'arquivos_extraidos'
  arquivo_zip.extractall(caminho_dir_extrair)

# Lista todos os arquivos do diretório 'arquivos_extraidos'
print('Arquivos extraídos:', [arquivo.name for arquivo in caminho_dir_extrair.iterdir()])

# Exclui o diretório 'arquivos_extraidos' e todos os arquivos contidos nele recursivamente
rmtree(caminho_dir_extrair)
