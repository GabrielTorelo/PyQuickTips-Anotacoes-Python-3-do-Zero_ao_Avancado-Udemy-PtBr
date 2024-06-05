# Importa o módulo os (usado para manipular o sistema operacional)
from os import path

# Importa o módulo pathlib (usado para manipular caminhos de arquivos)
from pathlib import Path

# Importa o módulo selenium (usado para automação de testes em navegadores)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Importa o módulo time (usado para manipular a execução do script)
from time import sleep

# Define um tempo de espera
TEMPO_ESPERA = 10

# Captura o caminho absoluto do arquivo
caminho = path.abspath('.')

print('Caminho absoluto:', caminho)

# Concatena o caminho absoluto com o diretório e o arquivo do chromedriver
CHROMEDRIVER_PATH = Path(caminho) / 'chromedriver/chromedriver.exe'

print('Caminho do chromedriver:', CHROMEDRIVER_PATH)

# Configura o chromedriver
chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=str(CHROMEDRIVER_PATH))
chrome_browser = webdriver.Chrome(
  service=chrome_service,
  options=chrome_options
)

# Abre o navegador e acessa o site do Google
chrome_browser.get('https://www.google.com')

# Aguarda até 10 segundos encontrar o campo de busca
# Obs: Pode ocorrer do campo de busca não ser encontrado
busca = WebDriverWait(chrome_browser, TEMPO_ESPERA).until(

  # Aguarda encontrar o campo de busca pelo nome 'q'
  EC.presence_of_element_located(
    (By.NAME, 'q') # Nome do campo de busca
  )
)

try: # Tenta realizar uma ação
  busca.send_keys('Python') # Digita 'Python' no campo de busca
  busca.send_keys(Keys.ENTER)
except Exception as e: # Se ocorrer um erro
  print('O campo de busca não foi encontrado:', e)

# Aguarda até 10 segundos encontrar o campo de pesquisa
# Obs: Pode ocorrer do campo de pesquisa não ser encontrado
pesquisa = WebDriverWait(chrome_browser, TEMPO_ESPERA).until(

  # Aguarda encontrar o campo de busca pelo ID 'search'
  EC.presence_of_element_located(
    (By.ID, 'search') # ID do campo de busca
  )
)

try: # Tenta realizar uma ação

  # Captura todos os links da pesquisa
  links = pesquisa.find_elements(By.TAG_NAME, 'a')

  # Clicka no primeiro link da pesquisa
  links[0].click()
except Exception as e: # Se ocorrer um erro
  print('O campo de pesquisa não foi encontrado:', e)

sleep(TEMPO_ESPERA)
