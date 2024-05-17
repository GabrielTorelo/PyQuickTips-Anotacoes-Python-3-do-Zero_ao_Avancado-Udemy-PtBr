# Criando um dicionário
contatos = {
  'Alice': '1234-5678',
  'Marcos': '8765-4321',
  'Carol': '5678-1234'
}

contatos['Davi'] = '4321-8765' # Adiciona um novo item ao dicionário

print(contatos['Alice']) # Imprime o valor associado à chave 'Alice'
print(contatos) # Imprime o dicionário completo

# Verificando se uma chave existe no dicionário
if 'Marcos' in contatos:
  print('Marcos está na lista de contatos. \n')
else:
  print('Marcos não está na lista de contatos. \n')

# Iterando sobre um dicionário
for nome, telefone in contatos.items(): # Para cada item no dicionário
  print(f'{nome}: {telefone}') # Imprime o nome e o telefone

# --------------------------------------------

print('\n')

# --------------------------------------------

pessoas = {} # Cria um dicionário vazio

# Adiciona um dicionário (Alice) ao dicionário pessoas
pessoas['Alice'] = {
  'telefone': '1234-5678',
  'email': 'alice@gmail.com'
}

# Adiciona outro dicionário (Marcos) ao dicionário pessoas
pessoas['Marcos'] = {
  'telefone': '8765-4321',
  'email': 'marcos@gmail.com'
}

# Adiciona outro dicionário (Carol) ao dicionário pessoas
pessoas['Carol'] = {
  'telefone': '5678-1234',
  'email': 'carol@gmail.com'
}

print(pessoas, '\n') # Imprime o dicionário completo

# Iterando sobre um dicionário
for nome, dados in pessoas.items(): # Para cada item no dicionário
  print(f'{nome}: {dados}') # Imprime o nome e os itens
