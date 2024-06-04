# Importa o módulo os (usado para manipular o sistema operacional)
from os import environ

# Importa o módulo dotenv (usado para carregar variáveis de ambiente de um arquivo .env)
# Deve ser instalado em seu ambiente virtual com o comando: pip install python-dotenv
from dotenv import load_dotenv, dotenv_values

# Importa o módulo string (usado para criar um Template)
from string import Template

# Importa o módulo email.mime.multipart (usado para criar um email)
from email.mime.multipart import MIMEMultipart

# Importa o módulo email.mime.text (usado para criar o corpo do email)
from email.mime.text import MIMEText

# Importa o módulo smtplib (usado para enviar o email)
from smtplib import SMTP

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Armazena as variáveis de ambiente (caso não exista alguma delas é retornada uma string vazia)
smtp_email = environ.get("SMTP_EMAIL", '')
smtp_password = environ.get("SMTP_PASSWORD", '')
smtp_server = environ.get("SMTP_SERVER", '')
smtp_port = environ.get("SMTP_PORT", '')

print(f'SMTP_EMAIL: {smtp_email}')
print(f'SMTP_PASSWORD: {smtp_password}')
print(f'SMTP_SERVER: {smtp_server}')
print(f'SMTP_PORT: {smtp_port}')

# Define o email do destinatário
destinatario = 'teste@testado.com.br'

print(f'Destinatário: {destinatario}')

# Cria uma string vazia para armazenar o texto do arquivo
mensagem = ""

try:
  # Abre o arquivo em modo leitura
  with open('aula102.html', 'r') as arquivo:

    # Lê o conteúdo do arquivo e armazena na variável
    texto = arquivo.read()

    # Cria um Template com o texto do arquivo
    template = Template(texto)

    # Substitui a variável no texto do arquivo pelo nome Gabriel
    mensagem = template.substitute(nome='Gabriel')
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao abrir o arquivo:', e)

print(mensagem)

# Cria um objeto MIMEText com o corpo do email
corpo_email = MIMEText(mensagem, 'html', 'utf-8')

# Cria um objeto MIMEMultipart
mime = MIMEMultipart()
mime['From'] = smtp_email # Remetente
mime['To'] = destinatario # Destinatário
mime['Subject'] = 'Teste de envio de email' # Assunto

# Adiciona o corpo do email ao objeto MIMEMultipart
mime.attach(corpo_email)

try:
  with SMTP(smtp_server, smtp_port) as servidor:
    # Informa ao servidor que é uma conexão de um cliente
    servidor.ehlo()

    # Inicia a criptografia da conexão
    servidor.starttls()

    # Conecta ao servidor SMTP com o email e a senha
    servidor.login(smtp_email, smtp_password)

    # Envia o email
    servidor.send_message(mime)

    print('Email enviado com sucesso!')
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao enviar o email:', e)
