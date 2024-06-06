# Importa o módulo os (usado para manipular o sistema operacional)
from os import path

# Importa o módulo PyPDF2 (usado para manipular arquivos PDF)
from PyPDF2 import PdfReader, PdfWriter

# Captura o caminho absoluto do arquivo
caminho = path.abspath('.')

print('Caminho absoluto:', caminho)

# Concatena o caminho absoluto com o diretório e o PDF desejado
PDF_PATH = path.join(caminho, 'aula111.pdf')

print('Caminho do PDF:', PDF_PATH)

try:
  # Abre o arquivo PDF em modo leitura
  leitor = PdfReader(PDF_PATH)

  # Captura a segunda página do PDF
  pagina_2 = leitor.pages[1]

  print('\nPDF aberto com sucesso!\n')

  # Instancia um objeto PdfWriter (escritor)
  escritor = PdfWriter()

  # Adiciona a segunda página ao objeto escritor
  escritor.add_page(pagina_2)

  # Cria um novo arquivo PDF com a segunda página
  with open('aula112.pdf', 'wb') as arquivo:
    escritor.write(arquivo)
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao abrir o PDF:', e)
