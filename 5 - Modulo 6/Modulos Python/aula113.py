# Importa o módulo os (usado para manipular o sistema operacional)
from os import path

# Importa o módulo PyPDF2 (usado para manipular arquivos PDF)
from PyPDF2 import PdfReader, PdfMerger

# Captura o caminho absoluto do arquivo
caminho = path.abspath('.')

print('Caminho absoluto:', caminho)

# Concatena o caminho absoluto com o diretório do primeiro PDF
PDF_1_PATH = path.join(caminho, 'aula111.pdf')

print('Caminho do PDF 1:', PDF_1_PATH)

# Concatena o caminho absoluto com o diretório do segundo PDF
PDF_2_PATH = path.join(caminho, 'aula112.pdf')

print('Caminho do PDF 2:', PDF_2_PATH)

# Lista com os caminhos dos arquivos PDF
arquivos = [
  PDF_2_PATH,
  PDF_1_PATH
]

try:
  # Abre o primeiro arquivo PDF em modo leitura
  leitor_1 = PdfReader(PDF_1_PATH)

  # Abre o segundo arquivo PDF em modo leitura
  leitor_2 = PdfReader(PDF_2_PATH)

  print('\nPDF aberto com sucesso!\n')

  # Instancia um objeto PdfMerger (mesclador)
  mesclador = PdfMerger()

  # Adiciona os dois arquivos PDF ao objeto mesclador
  for arquivo in arquivos:
    mesclador.append(arquivo)

  # Cria um novo arquivo PDF com os dois arquivos mesclados
  with open('aula113.pdf', 'wb') as pdf:
    mesclador.write(pdf)
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao abrir o PDF:', e)
