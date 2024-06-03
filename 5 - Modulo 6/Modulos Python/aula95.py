# Importa o módulo json (usado para manipular arquivos JSON)
from json import load, dump

# Define um dicionário
dicionario = {
  "nome": "Gabriel",
  "sobrenome": "Torelo",
  "sobrenome": "Torelo",
  "idade": 24,
  "altura": 1.8,
  "dev": True
}

try:
  # Abre o arquivo JSON para escrita
  with open('aula95.json', 'w') as arquivo:

    # Convertendo o dicionário para uma string JSON e salvando no arquivo
    dump(dicionario, arquivo, ensure_ascii=False, indent=2)
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao carregar JSON:', e)

# --------------------------------------------

print('\n')

# --------------------------------------------

try:
  # Abre o arquivo JSON para leitura
  with open('aula95.json', 'r') as arquivo:

    # Carrega o conteúdo do arquivo em um dicionário
    dicionario = load(arquivo)
    print(f'Dicionario: {dicionario}\n')
except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao carregar JSON:', e)
