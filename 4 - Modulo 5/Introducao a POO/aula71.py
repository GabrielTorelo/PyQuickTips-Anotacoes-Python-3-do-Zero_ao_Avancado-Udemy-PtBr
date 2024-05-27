# Importando as bibliotecas necessárias
from contextlib import contextmanager # Biblioteca para criar um gerenciador de contexto
from io import UnsupportedOperation # Biblioteca para tratar operações não suportadas

@contextmanager # Decorador para criar um gerenciador de contexto
def abrir(arquivo, modo):
  try:
    print('Abrindo o arquivo...')
    file = open(arquivo, modo, encoding='utf8') # Abrindo o arquivo
    yield file # Retornando o arquivo
  finally:
    print('\nFechando o arquivo...')
    file.close() # Fechando o arquivo

try:
  with abrir('aula71.txt', 'r') as arquivo: # Utilizando o bloco "with" para chamar a função "abrir", no qual retorna o arquivo aberto
    print(f'1ª linha: {arquivo.readline()}', end='') # Lendo a 1ª linha do arquivo
    lines = arquivo.readlines() # Lendo as linhas restantes do arquivo
    
    print('\nRestante do conteúdo do arquivo:')
    
    # Imprimindo o conteúdo do arquivo
    for line in lines:
      print(line, end='')

    arquivo.write('Escrevendo no arquivo...') # Tentando escrever no arquivo
except PermissionError as e:
  print(f'\nPermissão negada: {e}')
except UnsupportedOperation as e:
  print(f'\nOperação não suportada: {e}')
