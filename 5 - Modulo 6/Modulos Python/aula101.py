# Importa o módulo os (usado para manipular o sistema operacional)
from os import environ

# Importa o módulo dotenv (usado para carregar variáveis de ambiente)
# Deve ser instalado em seu ambiente virtual com o comando: pip install python-dotenv
from dotenv import load_dotenv, dotenv_values

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Armazena as variáveis de ambiente em um dicionário
variaveis = dotenv_values()

print(variaveis)

# Acessa a variável de ambiente BD_USER
usuario = environ.get('BD_USER')

print(f'BD_USER: {usuario}')

# Acessa a variável de ambiente BD_PASSWORD
senha = environ.get('BD_PASSWORD')

print(f'BD_PASS: {senha}')

# Acessa a variável de ambiente BD_PORT
porta = environ.get('BD_PORT')

print(f'BD_PORT: {porta}')

# Acessa a variável de ambiente BD_HOST
host = environ.get('BD_HOST')

print(f'BD_HOST: {host}')
