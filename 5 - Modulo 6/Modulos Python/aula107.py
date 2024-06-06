# Importa o módulo subprocess (usado para executar comandos do sistema operacional)
from subprocess import run, Popen
from sys import platform

# Imprime o sistema operacional
print(f'Sistema Operacional: {platform}\n')

# Exibe uma linha de separação
print('-' * 50, '\n')

# Define uma lista de comandos
comandos = [
  'ping 127.0.0.1', # Comando para verificar a conexão com a internet
  'dir', # Comando para listar os arquivos de um diretório
  'ipconfig', # Comando para verificar as configurações de rede
  'systeminfo' # Comando para verificar as informações do sistema
]

# Itera sobre a lista de comandos
for comando in comandos:
  processo = run(
    comando, # Executa cada comando da lista
    shell=True, # Executa o comando no shell
    capture_output=True, # Captura a saída do comando
    text=True, # Converte a saída do comando para texto
    encoding='cp850' # Define a codificação da saída do comando (win32)
  )

  # Captura a saída do comando
  saida = processo.stdout

  # Captura o código de retorno do comando
  retorno = processo.returncode
  
  # Captura os argumentos do comando
  argumentos = processo.args

  print(f'Comando: {comando}\n\nSaida:\n{saida}\n')
  print(f'Argumentos: {argumentos}')
  print(f'Retorno: {retorno}\n')

  # Exibe uma linha de separação
  print('-' * 50, '\n')

# Executa o comando 'ipconfig' em segundo plano
executar = Popen(
  'ipconfig',
  shell=True,
  text=True,
  encoding='cp850'
)
