# Importa o módulo os (usado para manipular o sistema operacional)
from os import system, path

# Importa a função sleep do módulo time (usado para pausar a execução do programa)
from time import sleep

print('Sujando a tela...')
print('A' * 1000) # Imprime 1000 letras 'A'

sleep(1) # Pausa a execução do programa por 1 segundos

print('\nLimpando a tela...')
sleep(0.8) # Pausa a execução do programa por 0.8 segundos
system('clear') # Limpa a tela do terminal

# --------------------------------------------
# --------------------------------------------

# Criando um caminho de arquivo
caminho = path.join('Users', 'USER', 'Downloads')
arquivo = path.join(caminho, 'arquivo.txt')

print('Caminho do arquivo:', arquivo)

# Separa o caminho do arquivo do nome do arquivo
tupla_arquivo = path.split(arquivo)
caminho, arquivo = tupla_arquivo

print('\nCaminho + Arquivo:', tupla_arquivo)
print('\nCaminho do arquivo:', caminho)
print('Nome do arquivo:', arquivo)

# Verifica se o arquivo existe
arquivo_existe = path.exists(arquivo)

print('\nO arquivo existe?', arquivo_existe)

# Captura o nome base do arquivo
nome_base = path.basename(arquivo)

# Captura o diretório base do arquivo
diretorio_base = path.basename(caminho)

print('\nNome base do arquivo:', nome_base)
print('Diretório base:', diretorio_base)

# Captura a extensão do arquivo
extensao = path.splitext(arquivo)[1]

print('\nExtensão do arquivo:', extensao)
