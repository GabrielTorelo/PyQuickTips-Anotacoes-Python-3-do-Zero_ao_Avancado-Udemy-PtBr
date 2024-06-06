# Importa o módulo os (usado para manipular o sistema operacional)
from os import path

# Importa o módulo PyPDF2 (usado para manipular arquivos PDF)
from PyPDF2 import PdfReader

# Captura o caminho absoluto do arquivo
caminho = path.abspath('.')

print('Caminho absoluto:', caminho)

# Concatena o caminho absoluto com o diretório e o PDF desejado
PDF_PATH = path.join(caminho, 'aula111.pdf')

print('Caminho do PDF:', PDF_PATH)

try:
  # Abre o arquivo PDF em modo leitura
  leitor = PdfReader(PDF_PATH)

  # Captura o número de páginas do PDF
  num_paginas = len(leitor.pages)

  # Captura a primeira página do PDF
  pagina_1 = leitor.pages[0]

  print('\nPDF aberto com sucesso!\n')

  print('Título:', leitor.metadata.get('/Title'))
  print('Número de páginas:', num_paginas)
  print(f'\nTexto da primeira página:\n{pagina_1.extract_text()}')
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao abrir o PDF:', e)
