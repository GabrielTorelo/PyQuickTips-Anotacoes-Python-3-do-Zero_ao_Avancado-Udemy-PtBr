from json import JSONDecodeError, dump, load

"""
  Salve os dados da sua classe em JSON e depois crie novamente
  as instâncias da classe com os dados salvos

"""

# Função para salvar o arquivo JSON
def salvar_arquivo(dados: object):
  try:
    with open('exercicio28.json', 'w', encoding='utf8') as arquivo: # Abre o arquivo para escrita
      dump(dados.__dict__, arquivo, indent=2, ensure_ascii=False)
      print('Dados salvos com sucesso!')
  except PermissionError: # Se não tiver permissão para salvar o arquivo
    print('Dados não foram salvos! Você não tem permissão para salvar arquivos!')
  except Exception: # Se ocorrer um erro inesperado ao salvar o arquivo
    print('Dados não foram salvos! Ocorreu um erro inesperado ao tentar salvar o arquivo!')

# Função para ler o arquivo JSON
def ler_arquivo(dados=None):
  try:
    with open('exercicio28.json', 'r', encoding='utf8') as arquivo: # Abre o arquivo para leitura
      dados = Pessoa(**load(arquivo))
      print('Dados carregados com sucesso!')
  except FileNotFoundError: # Se o arquivo não for encontrado
    print('Dados salvos não encontrados! O arquivo não foi encontrado!')
  except JSONDecodeError: # Se o arquivo estiver vazio ou não estiver no formato JSON
    print('Dados salvos não encontrados! O arquivo está vazio ou não está no formato JSON!')
  except Exception: # Se ocorrer um erro inesperado ao ler o arquivo
    print('Dados salvos não encontrados! Ocorreu um erro inesperado ao tentar ler o arquivo!')

  return dados

# Função para criar uma nova pessoa
def criar_pessoa():
  print('\n.: Criando novos dados para a pessoa :.')
  nome = input('Informe o nome: ').title()
  sobrenome = input('Informe o sobrenome: ').title()
  idade = int(input('Informe a idade: '))

  return Pessoa(nome, sobrenome, idade)

# Criando a classe Pessoa
class Pessoa:
  def __init__(self, nome, sobrenome, idade):
    self.nome = nome
    self.sobrenome = sobrenome
    self.idade = idade

  # Método para representar a classe (retorna uma string ao chamar a classe)
  def __str__(self):
    return f'{self.nome} {self.sobrenome} possui {self.idade} anos'

while True:
  user_input = input('Deseja carregar os dados salvos? [S]im | [N]ão: ').lower()

  if user_input == 's': # Se deseja carregar os dados salvos
    p1 = ler_arquivo() # Carrega os dados salvos em JSON

    if p1 == None:
      p1 = criar_pessoa() # Se não houver dados salvos, cria uma nova pessoa
    
    break
  elif user_input == 'n': # Se não deseja carregar os dados salvos
    p1 = criar_pessoa() # Cria uma nova pessoa
    break
  else: # Se opção inválida
    print('Opção inválida!\n')
    continue

# Exibindo os dados da classe
print(f'\n{p1}')

while True:
  ask_user = input('\nDeseja salvar os dados? [S]im | [N]ão: ').lower()

  if ask_user == 's': # Se deseja salvar os dados
    salvar_arquivo(p1) # Salva os dados da classe em JSON
  elif ask_user == 'n': # Se não deseja salvar os dados
    print('Dados não salvos!')
  else: # Se opção inválida
    print('Opção inválida!')
    continue

  print('\nAté mais!\n')
  break
