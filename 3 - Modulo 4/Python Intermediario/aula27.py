pessoas = {} # Cria um dicionário vazio

# Adiciona um dicionário (Alice) ao dicionário pessoas
pessoas['Carol'] = {
  'telefone': '5678-1234',
  'email': 'carol@gmail.com'
}

print('Carol: ', pessoas.get('Carol')) # Imprime o dados associado à chave 'Carol'

# --------------------------------------------

print('\n')

# --------------------------------------------

print('Carol: ', pessoas.pop('Carol')) # Remove e imprime o dicionário associado à chave 'Carol'
print(pessoas) # Imprime o dicionário completo

# --------------------------------------------

print('\n')

# --------------------------------------------

# Adiciona um dicionário (Marcos) ao dicionário pessoas
pessoas['Marcos'] = {
  'telefone': '8765-4321',
  'email': 'marcos@gmail.com'
}

# Adiciona outro dicionário (Alice) ao dicionário pessoas
pessoas['Alice'] = {
  'telefone': '1234-5678',
  'email': 'alice@gmail.com'
}

print('Último (removido): ', pessoas.popitem()) # Remove e imprime o último dicionário adicionado
print(pessoas) # Imprime o dicionário completo

# --------------------------------------------

print('\n')

# --------------------------------------------

# Cria um dicionário com outras pessoas (atualiza os dados do Marcos e adiciona Carol e Alice)
outras_pessoas = {
  'Carol': {
    'telefone': '5678-1234',
    'email': 'carolina@gmail.com'
  },
  'Marcos': {
    'telefone': '1234-5678',
    'email': 'marc2024@gmail.com'
  },
  'Alice': {
    'telefone': '8765-4321',
    'email': 'alice2024@gmail.com'
  }
}

pessoas.update(outras_pessoas) # Atualiza o dicionário pessoas com o dicionário outras_pessoas
print(pessoas) # Imprime o dicionário completo
