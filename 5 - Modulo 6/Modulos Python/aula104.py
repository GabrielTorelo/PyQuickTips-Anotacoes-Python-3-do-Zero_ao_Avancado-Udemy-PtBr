# Importa o módulo requests (usado para fazer requisições HTTP)
from requests import get

# URL que será acessada
URL = 'https://www.SITE_QUALQUER.com.br'

# Realiza a requisição GET para a URL
RESPOSTA = get(URL)

# Encontra o título da página
inicio_titulo = RESPOSTA.text.find('<title>') + 7
fim_titulo = RESPOSTA.text.find('</title>')

# Extrai o título da página
tiulo = RESPOSTA.text.strip()[inicio_titulo:fim_titulo]

print(f'Status code: {RESPOSTA.status_code} | URL: {RESPOSTA.url} | Título: {tiulo}')
