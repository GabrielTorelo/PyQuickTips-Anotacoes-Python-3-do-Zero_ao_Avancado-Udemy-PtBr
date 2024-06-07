# Importa o módulo os (usado para manipular o sistema operacional)
from os import path

# Importa o módulo PIL (usado para manipular imagens)
from PIL import Image

# Captura o caminho absoluto do arquivo
caminho = path.abspath('.')

print('Caminho absoluto:', caminho)

# Define o caminho da imagem
caminho_imagem = path.join(caminho, 'aula118_original.jpg')

# Define o novo caminho da imagem (após redimensionamento)
novo_caminho_imagem = path.join(caminho, 'aula118_novo.jpg')

try:
  print('Abrindo a imagem...')

  # Abre a imagem no caminho especificado
  imagem = Image.open(caminho_imagem)
  
  print('\nImagem aberta com sucesso!')

  # Exibe informações da imagem
  print('\nFormato da imagem:', imagem.format)
  print('Modo da imagem:', imagem.mode)
  print('Tamanho original da imagem:', imagem.size)

  print('\nRedimensionando a imagem (W: 640px)! Aguarde...')

  # Captura a largura e altura original da imagem
  largura_original, altura_original = imagem.size

  # Define as novas dimensões da imagem
  largura = 640
  altura = round((altura_original * largura) / largura_original)

  # Redimensiona a imagem
  nova_imagem = imagem.resize(size=(largura, altura))
  
  print('\nImagem redimensionada com sucesso!')
  print('Novo tamanho da imagem:', nova_imagem.size)

  print('\nSalvando a imagem redimensionada! Aguarde...')

  # Salva a imagem redimensionada no novo caminho
  nova_imagem.save(
    novo_caminho_imagem,
    optimize=True,
    quality=70,
  )

  print('\nImagem redimensionada salva com sucesso!')
  print('Tamanho original do arquivo:', round(path.getsize(caminho_imagem) / 1024, 2), 'KB')
  print('Novo tamanho do arquivo:', round(path.getsize(novo_caminho_imagem) / 1024, 2), 'KB')

except Exception as e: # Trata caso ocorra algum erro
  print('\nErro ao redimensionar a imagem:', e)
