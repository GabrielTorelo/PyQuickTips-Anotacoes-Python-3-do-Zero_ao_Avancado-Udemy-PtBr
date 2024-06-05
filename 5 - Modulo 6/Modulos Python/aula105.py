# Importa o módulo requests (usado para fazer requisições HTTP)
from requests import get

# Importa o módulo bs4 (usado para fazer parse de HTML)
from bs4 import BeautifulSoup

# URL que será acessada
URL = 'https://www.SITE_QUALQUER.com.br'

# Realiza a requisição GET para a URL
RESPOSTA = get(URL)

# Pega o conteúdo da resposta e faz o parse do HTML para string
RESPOSTA_CRUA = RESPOSTA.text

# Faz o parse do HTML
HTML = BeautifulSoup(RESPOSTA_CRUA, 'html.parser')

# Verifica se o título da página foi encontrado
if HTML.title is None:
  titulo = 'Título não encontrado!'
else:
  # Captura o texto do título
  titulo = HTML.title.text

print(f'Status code: {RESPOSTA.status_code} | URL: {RESPOSTA.url} | Título: {titulo}')

# --------------------------------------------

print('\n')

# --------------------------------------------

# Pega o conteúdo do primeiro 'b' dentro de 'html / body / div / div / nobr'
primeiro_b = HTML.select_one('html > body > div > div > nobr > b')

# Verifica se o conteúdo foi encontrado
if primeiro_b is None:
  primeiro_b = 'Texto não encontrado!'
else:
  # Captura o texto do primeiro b
  primeiro_b = primeiro_b.text

print(f'Texto: {primeiro_b}')
