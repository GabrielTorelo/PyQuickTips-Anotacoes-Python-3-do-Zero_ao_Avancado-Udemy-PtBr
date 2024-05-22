from json import dump, load

# Dicionário
pessoa = {
  'nome': 'Gabriel',
  'sobrenome': 'Torelo',
  'enderecos': [
    {'rua': 'Rua das Ruas', 'numero': 123},
    {'rua': 'Rua das Ruas', 'numero': 321},
  ],
  'altura': 1.8,
  'numeros_preferidos': (2, 4, 6, 8, 10),
  'dev': True
}

pessoas = {} #Cria um dicionário vazio

caminho_arquivo = 'aula44.json' # Caminho do arquivo (.json)

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo: # Abre o arquivo para escrita
  dump(pessoa, arquivo, ensure_ascii=False, indent=True) # Salva o dicionário no arquivo

with open(caminho_arquivo, 'r', encoding='utf8') as arquivo: # Abre o arquivo para leitura
  pessoas = load(arquivo) # Carrega o arquivo para o dicionário

print(pessoas) # Imprime o dicionário
