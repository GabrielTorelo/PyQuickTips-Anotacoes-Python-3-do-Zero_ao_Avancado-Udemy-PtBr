# Importa o módulo string (usado para manipular strings)
from string import Template, ascii_letters, digits, punctuation

# Dicionário com as variáveis que serão substituídas no texto
dicionario = dict(
  convidado_nome = 'Gabriel',
  empresa_nome = 'Empresa Bonita',
  empresa_anos = '10',
  evento_data = '04/06/2024',
  evento_inicio = '13:00h',
  evento_fim = '17:00h',
  evento_endereco = 'Rua do evento, 123',
  evento_valor = '1kg de alimento não perecível',
  evento_brinde = 'camiseta e caneca'
)

# Cria uma string vazia para armazenar o texto do arquivo
mensagem = ""

try:
  # Abre o arquivo em modo leitura
  with open('aula100.txt', 'r') as arquivo:

    # Lê o conteúdo do arquivo e armazena na variável
    texto = arquivo.read()

    # Cria um Template com o texto do arquivo
    template = Template(texto)

    # Substitui as variáveis no texto do arquivo pelo conteúdo do dicionário
    mensagem = template.substitute(dicionario)
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao abrir o arquivo:', e)

print(mensagem)

# --------------------------------------------

print('\n')

# --------------------------------------------

# Cria uma string com as letras do alfabeto (maiúsculas e minúsculas)
letras_maiusculas_minusculas = ascii_letters

print('Letras do alfabeto (maiúsculas e minúsculas):', letras_maiusculas_minusculas)

# Cria uma string com os dígitos
digitos = digits

print('Dígitos:', digitos)

# Cria uma string com os caracteres especiais
caracteres_especiais = punctuation

print('Caracteres especiais:', caracteres_especiais)
